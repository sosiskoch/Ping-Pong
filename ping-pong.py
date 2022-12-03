from pygame import *

W_W = 700
W_H = 500

window = display.set_mode((W_W, W_H))
display.set_caption("Пинг-Понг")
background = image.load("back.jpeg")
background = transform.scale(background, (W_W, W_H))

clock = time.Clock()

game = True
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    display.update()