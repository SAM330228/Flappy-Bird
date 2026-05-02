from pygame import *
from random import *
#Создание окна и тд.
Finished = False
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
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__(player_image, player_x, player_y, width, height, player_speed)
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

Bird = Player('pony.jpg', 300, 200, 50, 50, 5)

class Wall(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__(player_image, player_x, player_y, width, height, player_speed)
        self.passed = False


    def spawn1(self):
        global score
        self.rect.x = 800 + 150
        self.passed = False
        self.rect.y = randint(-10, 0) 
        score += 1
    
    def spawn2(self):
        self.rect.x = 800 + 150
        self.passed = False
        self.rect.y = randint(300, 450)

    def update1(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.spawn1()

    def update2(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.spawn2()

wall2 = Wall('T2.png', 710, -50, 65, 200, 5)
wall1 = Wall('T1.png', 710, 300, 65, 200, 5)
#игра
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not Finished:
        screen.blit(background, (0, 0))
        
        Bird.update()
        Bird.reset()

        wall1.update2()
        wall1.reset()

        wall2.update1()
        wall2.reset()

        draw.rect(screen, (0, 0, 255), wall1.rect, 2)
        draw.rect(screen, (0, 0, 255), wall2.rect, 2)
        draw.rect(screen, (0, 255, 0), Bird.rect, 2)

        scored = font1.render(f"Счет: {score}", True, (255, 200, 255))
        screen.blit(scored, (10, 10))

        if sprite.collide_rect(Bird, wall1) or sprite.collide_rect(Bird, wall2):
            Finished = True
    else:
        lose = font1.render("Вы проиграли", True, (128, 0, 0))
        screen.blit(lose, (x // 2 - 125, y // 2 - 50))

    clock.tick(FPS)
    display.update()
    
