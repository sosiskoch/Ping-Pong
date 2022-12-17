from pygame import *
import time as t


W_W = 700
W_H = 500
FPS = 60
BG_COLOR = (0, 255, 239)

window = display.set_mode((W_W , W_H))
display.set_caption('Пинг-Понг')

#Class
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, image_name):
        self.img = image.load(image_name)
        self.img = transform.scale(self.img, (w, h))
        self.rect = Rect(x, y, w ,h)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y+30 >= W_H:
            self.speed_y *= -1
        if self.rect.x+30 >= W_W:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
        if self.rect.x < 0:
            self.speed_x *= -1
        super().update()

class Player(GameSprite):
    def __init__(self, x, y, w, h, speed, image_name, k_up, k_down):
        super().__init__(x, y, w, h, speed, image_name)
        self.k_up = k_up
        self.k_down = k_down

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.k_up]:
            if self.rect.y - self.speed_y > 0:
                self.rect.y -= self.speed_y
        elif key_pressed[self.k_down]:
            if self.rect.y + self.speed_y + self.rect.h < W_H:
                self.rect.y += self.speed_y
        super().update()

ball = Ball(50, 50, 30, 30, 3, 'ball_prev_ui.png')
player1 = Player(0, 200, 20, 100, 5, 'bob.png', K_w, K_s)
player2 = Player(678, 200, 20, 100, 5, 'bob.png', K_UP, K_DOWN)

clock = time.Clock()

game = True
while game:
    clock.tick(FPS)


    for e in event.get():
        if e.type == QUIT:
            game = False

    #Правила
    if player1.rect.colliderect(ball.rect):
        ball.speed_x *= -1
    if player2.rect.colliderect(ball.rect):
        ball.speed_x *= -1

    #отрисовка
    window.fill(BG_COLOR)
    ball.update()
    player1.update()
    player2.update()
    display.update()
