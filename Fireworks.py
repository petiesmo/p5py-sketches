from p5 import *

G = (0,0.25)
particles = None
hz = None

class Particle(Vector):
    def __init__(self,p,v,a):
        self.pos = Vector(*p)
        self.vel = Vector(*v)
        self.acc = Vector(*a)
        self.color = (255*random_uniform(), 255*random_uniform(), 255*random_uniform())

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        return None

    def show(self, size=3):
        stroke(255)
        fill(*self.color)
        circle(self.pos,size)
        return None

def setup():
    global G,particles,hz
    size(1000,1500)
    title('Fireworks')
    hz = height*2/3
    particles = [Particle((width*random_uniform(),height),(0,-20),G) for i in range(7)]
    return None

def draw():
    global G, particles,hz
    if random_uniform() < 0.1:
        particles.append(Particle((width*random_uniform(),hz),(0,-20),G))

    background(0)
    stroke(255)
    line((0,hz),(width,hz))
    
    for p in particles:
        p.update()
        
        if p.pos.y > 3*height/4:
            particles.remove(p)
        if p.vel.y > 0:
            p.show(size=20)
        else:
            p.show()

    return None
    

run()
    
