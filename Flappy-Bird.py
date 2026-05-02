from pygame import *
from random import *
#Создание окна и тд.
x = 700
y = 500
screen = display.set_mode((x,y))
display.set_caption('Pony-Bird')
background = transform.scale(image.load('clouds.png'),(x,y))
font.init()
font1 = font.SysFont('Вы проиграли', 36) 

#Классы, фукции
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        #Движение
        self.speed_y = self.speed
        self.rect.y += self.speed_y * 3 and self.rect.y < 435

        #Клавиши
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

Bird = Player('pony.jpg', 300, 200, 5)

class Wall(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def spawn(self):
        self.rect.x = 800 + 150

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.spawn()

wall2 = Wall('T1.png', 710, 30, 5)
wall1 = Wall('T1.png', 710, 470, 5)
walls = sprite.Group()
#игра
clock = time.Clock()
FPS = 60
game = True
while game:
    screen.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    Bird.update()
    Bird.reset()

    wall1.update()
    wall1.reset()

    wall2.update()
    wall2.reset()

    clock.tick(FPS)
    display.update()
