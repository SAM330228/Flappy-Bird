from pygame import *
#Создание окна и тд.
x = 700
y = 500
screen = display.set_mode((x,y))
display.set_caption('Pony-Bird')
background = transform.scale(image.load('clouds.png'),(x,y))
#Классы, фукции
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_fall, player_speed_up):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed_fall = player_speed_fall
        self.speed_up = player_speed_up
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        #Движение
        self.rect.y += self.speed_fall and self.rect.y < 435

        #Клавиши
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed_up
        
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_up

Bird = Player('pony.jpg', 300, 200, 25, 5)
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

    clock.tick(FPS)
    display.update()