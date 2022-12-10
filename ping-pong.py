from pygame import *

W_W = 700
W_H = 500

window = display.set_mode((W_W, W_H))
display.set_caption("Пинг-Понг")

#Class
class GameSprite(sprite.Sprite):
    def __init__(self, fn, x, y, w, h, speed):
        super().__init__()
        self.image = image.load(fn)
        self.image = transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.speed = speed
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ball = GameSprite("ball_prev_ui.png", 100, 100, 50, 50, 0)

clock = time.Clock()

game = True
while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False




    window.fill((255,255,255))
    ball.update()
    display.update()