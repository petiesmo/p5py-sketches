from p5 import *

img = None
res = 10
small_point = res/2
large_point = res

def setup():
    global img
    size(1024, 512)
    no_stroke()

    img = load_image("NASA-moon-flag.jpg")


def draw():
    global img, res, small_point, large_point
    background(10)
    for x in range(0,width,res):
        for y in range(0,height,res):
            pix = img._get_pixel((x,y))
            fill(pix,60)
            circle((x,y),random_uniform(small_point,large_point))
    #no_loop()



#Original example from p5 Schiffman
##def draw():
##    global img, large_point, small_point
##    #pointillize = remap(mouse_x, [0, width], [small_point, large_point])
##    pointillize = random_uniform(10,30)
##    x = floor(random_uniform(img.width))
##    y = floor(random_uniform(img.height))
##
##    pix = img._get_pixel((x, y))
##    fill(pix, 60)
##
##    ellipse((x, y), pointillize, pointillize)

if __name__ == '__main__':
    run(frame_rate = 1)

