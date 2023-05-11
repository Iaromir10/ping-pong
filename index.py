from pygame import *

#mixer.init()
#mixer.music.load()
#mixer.music.play()

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг понг')
background = transform.scale(image.load('dfasdfasdfasd.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        self.image = transform.scale(image.load(sprite_image), (70, 70))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 625:
            self.rect.x += self.speed
    def update right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < 625:
            self.rect.x += self.speed
        

player = Player('sprite-0.5.png', 5, 400, 10)

finish = False
game = True
clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 80)
won = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOH!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.update()

        player.reset()
        enemy.reset()
        gold.reset()

        
    display.update()
    clock.tick(FPS)
