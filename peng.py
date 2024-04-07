from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.h = h
        self.rect.w = w

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def bounty_r():
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-5-self.rect.width:
            self.rect.y += self.speed
    def bounty_l():
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 500-5-self.rect.width:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.speed_x = 0
        self.speed_y = 0

    def set_diretion(self,speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x*self.speed
        self.rect.y += self.speed_y*self.speed

    def check_direction(self,pl1,pl2):
        if self.rect.y<=0:
            self.seed_y*=-1
        elif self.rect.y>=self.rect.y>=500-self.rect.height:
            self.seed_y*=-1
        elif self.rect.spritecollide(pl1.rect):
            self.speed_x*=-1
        elif self.rect.spritecollide(pl2.rect):
            self.speed_x*=-1
        elif self.rect.x<=0:
            point_r+=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.x = 500/2-self.rect.height/2
        elif self.rect.x>=500-self.rect.width:
            point_l+=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.x = 500/2-self.rect.height/2        




point_l = 0
point_r = 0

ball = Ball('')

window = display.set_mode((700,500))
display.set_caption('Пэнг-Понг')

background = transform.scale(image.load('ostrov.jpg'), (700,500))

game = True
finish = True
clock = time.Clock()
FPS = 60

bounty_1 = Player('bounty_left.png', 70,70,50,150,5)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        window.blit(background,(0,0))
        bounty_1.update()
        bounty_1.reset()



        display.update()
        clock.tick(FPS)
