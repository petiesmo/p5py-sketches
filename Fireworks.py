from p5 import *

G = (0,0.25)
particles = None
hz = None

def polar2rect(r,th,deg=False):
	'''Conv 2d polar coords to x,y'''
	th = th*PI/180 if deg else th
	return (r*cos(th), r*sin(th))

class mdVector(Vector):
	def __init__(self,m,d,deg=False):
		x,y = polar2rect(m,d,deg)
		super().__init__(x,y)

class Particle():
    def __init__(self,p,v,a,e=False):
        self.pos = Vector(*p)
        self.vel = Vector(*v)
        self.acc = Vector(*a)
        self.color = (255*random_uniform(), 255*random_uniform(), 255*random_uniform())
		self.exploded = e
		self.children = []
		return None

    def update(self):
		for c in self.children:
			 
		self.vel += self.acc
        self.pos += self.vel
        return None

    def show(self, size=3):
        stroke(255)
        fill(*self.color)
        circle(self.pos,size)
		[circle(i.pos,4) for i in self.children]
        return None

	def explode(self,n):
		#Make list of new particles, with state = parent
		self.exploded = True
		self.children = []
		for i in range n:
			# New Particles get radial velocity, and some drag (neg radial acc)
			vfire = mdVector(10, 5*i, True)
			self.children.append(Particle(self.pos, self.vel+vfire, self.acc+self.drag(vfire),True))
		return None

		def drag(self, v):
			return mdVector(v.magnitude**2, v.direction+180,True)
#End Particle class
		

def setup():
    global G,particles,hz
    size(1000,1500)
    title('Fireworks')
    hz = height*2/3
    particles = [Particle((width*random_uniform(),height),(0,-20),G) for i in range(7)]
    return None

def draw():
    global G, particles,hz
	# New particles appear randomly
    if random_uniform() < 0.1:
        particles.append(Particle((width*random_uniform(),hz),(0,-20),G))

    background(0)
    stroke(255)
    line((0,hz),(width,hz))
    
    for p in particles:
        # New pos, vel, acc
		p.update()
        # Die off
        if p.pos.y > 3*height/4:
            particles.remove(p)
        # Boom!
		if p.vel.y > 0 and not p.exploded
            p.explode(20)
			p.show(size=20)	#TODO Replace with burst of new particles
        else:
            p.show()

    return None

    
if __name__=='__main__':
	run()