from p5 import *

img = None
img2 = None

def setup():
    global img
    size(1600, 1066)
    img = load_image("NASA-moon-flag.jpg")
    img2 = load_image("blood_moon.jpg")

    #img.mask(imgMask)
    image_mode("CENTER")

def draw():
    global img, img2
    background(0, 102, 153)
    image(img, (width / 2, height / 2))
    #tint(100,100)
    image(img2, (mouse_x, mouse_y))

if __name__ == '__main__':
    run()
