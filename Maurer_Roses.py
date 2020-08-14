from p5 import *

n = 8
d = 29
s = 300

def setup():
    size(1000,1000)
    title("Maurer Roses")

def draw():
    global n,d,s
    clear
    background(25)
    stroke(0,0,255)
    no_fill()
    translate(width/2, height/2)
    rotate(PI)
    #m = Vector(mouse_x,mouse_y)
    #s = .75*m.magnitude
    
    #Maurer Rose
    stroke(0,0,255)
    stroke_weight(2)
    begin_shape()
    for theta in range(181):
        k = d*theta * PI / 180
        r = s*sin(n*k)
        vertex(r*cos(k), r*sin(k))
    end_shape()
    #stroke(0,255,255)
    begin_shape()
    for theta in range(181,361):
        k = d*theta * PI / 180
        r = s*sin(n*k)
        vertex(r*cos(k), r*sin(k))
    end_shape()
    
    #Regular Rose
    stroke(255,0,0,150)
    stroke_weight(5)
    begin_shape()
    for theta in range(181):
        th = theta * PI / 180
        r = s*sin(n*th)
        vertex(r*cos(th), r*sin(th))
    end_shape()
    #stroke(0,255,0,150)
    begin_shape()
    for theta in range(181,361):
        k = theta * PI / 180
        r = s*sin(n*k)
        vertex(r*cos(k), r*sin(k))
    end_shape()

    no_loop()

def mouse_pressed():
    global n, d
    d += 2
    redraw()

if __name__ == '__main__':
    run()
    
