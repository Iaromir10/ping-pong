from pygame import *

#mixer.init()
#mixer.music.load()
#mixer.music.play()

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг понг')
background = transform.scale(image.load('Group 1.png'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, width, height):
        self.image = transform.scale(image.load(sprite_image), ( width, height))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 360:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 360:
            self.rect.y += self.speed
        

player1 = Player('1653439.512_prev_ui.png', 5, 200, 10, 20, 140)
player2 = Player('1653439.512_prev_ui.png', 660, 200, 10, 20, 140)
ball = GameSprite('pngwing.com (7).png', 330, 230, 300, 50, 50)

finish = False
game = True
clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 80)
won = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOH!', True, (180, 0, 0))

speed_x = 3
speed_y = 3   


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player1.update_left()
        player2.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y *= -1

        player1.reset()
        player2.reset()
        ball.reset()

        
    display.update()
    clock.tick(FPS)
