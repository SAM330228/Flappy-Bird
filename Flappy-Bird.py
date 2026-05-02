from pygame import *
from random import *
#Создание окна и тд.
score = 0
x = 700
y = 500
screen = display.set_mode((x,y))
display.set_caption('Pony-Bird')
background = transform.scale(image.load('clouds.png'),(x,y))
font.init()
font1 = font.SysFont('Arial', 36) 
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
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.velocity = 0  # Текущая скорость падения
        self.gravity = 0.6 # Сила притяжения (настрой под себя)
        self.jump_power = -10 # Сила прыжка

    def update(self):
        # 1. Гравитация постоянно тянет вниз
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # 2. Ограничение по нижней границе экрана
        if self.rect.y > 435:
            self.rect.y = 435
            self.velocity = 0

        keys = key.get_pressed()
        if (keys[K_w] or keys[K_UP]) and self.rect.y > 5:
            self.velocity = self.jump_power

Bird = Player('pony.jpg', 300, 200, 5)

class Wall(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)


    def spawn(self):
        global score
        self.rect.x = 800 + 150
        score += 0.5
        print('Счёт:',score)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.spawn()

def finish():
    None

wall2 = Wall('T2.png', 710, 200, 5)
wall1 = Wall('T1.png', 710, 400, 5)
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

    #Отрисовка текста. font1.render("Вы проиграли", True, (255, 0, 0))

    clock.tick(FPS)
    display.update()
    
