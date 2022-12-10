from pygame import *
import time as t

W_W = 700
W_H = 500

window = display.set_mode((W_W, W_H))
display.set_caption("Пинг-Понг")

#Class
class GameSprite(sprite.Sprite):
    def __init__(self, fn, x, y, w, h, speedx, speedy):
        super().__init__()
        self.image = image.load(fn)
        self.image = transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.speedx = speedx
        self.speedy = speedy
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] 


ball = GameSprite("ball_prev_ui.png", 100, 100, 40, 40, 3, 3)
stick1 = Player("stick_prev_ui.png", 647, 95, 80, 250, 3, 3)
clock = time.Clock()

game = True
while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False


    ball.rect.x += ball.speedx
    ball.rect.y += ball.speedy
    if ball.rect.y > W_H - 40 or ball.rect.y < 0:
        ball.speedy *= -1
    if ball.rect.x > W_W - 40 or ball.rect.x < 0:
        ball.speedx *= -1
        t.sleep(1)
        ball.rect.x = 350
        ball.rect.y = 250
        

    window.fill((255,255,255))
    ball.update()
    stick1.update()
    display.update()