from p5 import *
from random import randint as ri
from random import randrange as rr
from random import choice as rc

G = Vector(0,0.25)
particles = None
hzn = None
render_ratio = 3

def polar2rect(r,th,deg=False):
	'''Conv 2d polar coords to x,y'''
	th = th*PI/180 if deg else th
	return (r*cos(th), r*sin(th))

class mdVector(Vector):
	def __init__(self,m,d,deg=False):
		x,y = polar2rect(m,d,deg)
		super().__init__(x,y)

class Particle():
    def __init__(self,p,v,a,rgb=None,exp=False,numch=25):
        self.pos = Vector(*p)
        self.vel = Vector(*v)
        self.acc = Vector(*a)
        self.color = rgb if rgb is not None else (ri(0,255), ri(0,255), ri(0,255))
        self.exploded = exp
        if int(numch) > 0:
	        self.children = []
	        for i in range(numch):
	        # New Particles get radial velocity, and some drag (neg radial acc)
		        vfire = mdVector(rc([5,7,9]), ri(0,359), True)
	            self.children.append(Particle(self.pos, vfire, G, rgb=self.color, exp=False, numch=0))
        return None

    def update(self):
        self.acc = G #+ self.drag()
        self.vel += self.acc
        self.pos += self.vel
        return None

    def show(self, size=3):
        no_stroke()
        fill(*self.color)
        circle(self.pos,size)
        if self.exploded:
	        (ch.show(3) for ch in self.children)
        return None

    def explode(self,n):
        #Make list of new particles, with state = parent
        self.exploded = True
        # Assign parent velocity and position to Particles get radial velocity
	    for c in self.children:
	        c.pos += self.pos
	        c.vel += self.vel
        return None

    @property
    def drag(self):
        Cd = .0015
        return mdVector(Cd*self.vel.magnitude**2, self.vel.angle+PI, False)
			
#End Particle class
		

def setup():
    global G,particles,hzn
    size(1000,1500)
    title('Fireworks')
    hzn = height*2/3
    particles = [Particle((rr(width),hzn),(rr(-3,3),rr(-20,-15)),G) for i in range(3)]
    return None

def draw():
    global G, particles, hzn, render_ratio
	# New particles appear randomly
    if random_uniform() < 0.1:
        particles.append(Particle((rr(width),hzn),(rr(-3,3),rr(-30,-20)),G))

    background(0)
    stroke(255)
    line((0,hzn),(width,hzn))
    temp = []
    for r in range(render_ratio):
            for p in particles:
                # New pos, vel, acc
                p.update()
                # Boom!
                if p.vel.y > 0 and not p.exploded:
                    temp.extend(p.explode(30))# Burst of new particles
                # Die off
                if p.pos.y > 3*height/4:
                    particles.remove(p)
            # Add any new particles to the main array
            particles.extend(temp)
    for p in particles:
            # Display all points
            p.show(6)
    return None

    
if __name__=='__main__':
	run(frame_rate = 60/render_ratio)

	
