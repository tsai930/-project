from tarfile import XGLTYPE
import pygame
import random
import os
FPS=70 
WIDTH=500
HIGHT=600

BROWN=(139,69,19)
GREEN=(0,255,0)
WHITE=(255,255,255)
RED=(255,0,0)
#遊戲初始化 及 創建視窗
pygame.init()#初始化
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("小遊戲")
clock=pygame.time.Clock()

#載入圖片
background_img=pygame.image.load(os.path.join("img","background.jpg")).convert()
#rock_img=pygame.image.load(os.path.join("img","rock1.png")).convert()
player0=pygame.image.load(os.path.join("img","player.png ")).convert()
bullet0=pygame.image.load(os.path.join("img","bullet.png ")).convert()
rock0=pygame.image.load(os.path.join("img","rock0.png")).convert()
rock1=pygame.image.load(os.path.join("img","rock1.png")).convert()

font_name=pygame.font.match_font('arial')

def hitrock():
    r=Rock0()
    all_sprites.add(r)
    rocks.add(r)
def hitrock1():
    r1=Rock1()
    all_sprites.add(r1)
    rocks1.add(r1)

def cata():
    screen.blit(pygame.transform.scale(background_img,(500,600)),(0,0))
    text(screen,"BEEP U",50,WIDTH/2,30)
    text(screen,"a go left,d go right,space shoot",25,WIDTH/2,HIGHT/2)
    text(screen,"press to stard",40,WIDTH/2,HIGHT/2-50)
    text(screen,"+5 point",20,WIDTH/3-35,HIGHT*2/3-30)
    text(screen,"-3 point",20,WIDTH*2/3-20,HIGHT*2/3-30)
    text(screen,"point<0 lose",30,WIDTH/2,HIGHT*3/4+20)
    rock00=pygame.transform.scale(rock0,(55,35))
    rock00.set_colorkey((0,0,0))
    screen.blit(rock00,(WIDTH/3-50,HIGHT*2/3))
    rock11=pygame.transform.scale(rock1,(43,57))
    rock11.set_colorkey((0,0,0))
    screen.blit(rock11,(WIDTH*2/3-30,HIGHT*2/3))
    pygame.display.update()
    start=True
    while start:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                start=False

def word(sur,point,hp,size,xp,y,xh,):
    font=pygame.font.Font(font_name,size)
    surfacep=font.render(point,True,(0,0,0,))
    surfaceh=font.render(hp,True,(0,0,0))
    rectp=surfacep.get_rect()
    recth=surfaceh.get_rect()
    rectp.centerx=xp
    recth.centerx=xh
    recth.top=rectp.top=y
    sur.blit(surfaceh,recth)
    sur.blit(surfacep,rectp)

def text(sur,word,size,x,y):
    font=pygame.font.Font(font_name,size)
    surface=font.render(word,True,WHITE)
    rect=surface.get_rect()
    rect.centerx=x
    rect.top=y
    sur.blit(surface,rect)

def healthpoint(sur,hp,size,x,y):
    if int(hp) <=0:
        hp=0
    hp=str(hp)
    font=pygame.font.Font(font_name,size)
    surface=font.render(hp,True,GREEN)
    rect=surface.get_rect()
    rect.centerx=x
    rect.top=y
    sur.blit(surface,rect)
  
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player0,(60,49)) 
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.radius=30
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HIGHT-10
        self.speed=6
        self.health=5

    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x+=self.speed
        if key_pressed[pygame.K_a]:
            self.rect.x-=self.speed
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
  
class Rock0(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(rock0,(44,30))
        self.image.set_colorkey((0,0,0))        
        self.rect=self.image.get_rect()
        self.radius=self.rect.width*0.9/2
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speed=random.randrange(2,5)
        self.speedx=random.randrange(-4,4)
    def update(self):
        self.rect.y+=self.speed
        self.rect.x+=self.speedx
        if self.rect.top>HIGHT :#or self.rect.right<0 or self.rect.left>WIDTH:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speed=random.randrange(3,6)
            self.speedx=random.randrange(-4,4)
        elif self.rect.right<0 or self.rect.left>WIDTH:
            self.speedx=-self.speedx

class Rock1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(rock1,(43,57))
        self.image.set_colorkey((0,0,0))        
        self.rect=self.image.get_rect()
        self.radius=self.rect.width*0.9/2
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speed=random.randrange(2,5)
        self.speedx=random.randrange(-4,4)
    def update(self):
        self.rect.y+=self.speed
        self.rect.x+=self.speedx
        if self.rect.top>HIGHT :#or self.rect.right<0 or self.rect.left>WIDTH:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speed=random.randrange(3,6)
            self.speedx=random.randrange(-4,4)
        elif self.rect.right<0 or self.rect.left>WIDTH:
            self.speedx=-self.speedx

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bullet0,(30,30)) 
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.speed=random.randrange(-20,-15)

    def update(self):
        self.rect.y+=self.speed
        if self.rect.bottom<0:
            self.kill()
#遊戲迴圈
initial=True
running=True
while running:
    if initial:
        cata()
        #初始化
        all_sprites=pygame.sprite.Group()
        rocks1=pygame.sprite.Group()
        rocks=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        player=Player()
        all_sprites.add(player)
        for i in range(5):
            hitrock()
        for i in range(3):
            hitrock1()
        score=0
        initial=False
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()
    #更新遊戲
    all_sprites.update()
    hits=pygame.sprite.groupcollide(rocks,bullets,True,True)
    for hit in hits:
        score+=5
        hitrock()
    hits1=pygame.sprite.groupcollide(rocks1,bullets,True,True)
    for i in hits1:
        score-=3
        hitrock1()
    if score<0:
        score=0
        player.health=5
        initial=True


    hits=pygame.sprite.spritecollide(player,rocks,True,pygame.sprite.collide_circle)
    for i in hits:
        hitrock()
        player.health-=1
        if player.health<=0:
            player.health=5
            initial=True
    hitss=pygame.sprite.spritecollide(player,rocks1,True,pygame.sprite.collide_circle)
    for i in hitss:
        hitrock1()
        player.health-=1
        if player.health<=0:
            player.health=5
            initial=True
        

    #畫面顯示
    screen.blit(pygame.transform.scale(background_img,(500,600)),(0,0))
    all_sprites.draw(screen)
    word(screen,"piont","hp",20,WIDTH/2-30,10,WIDTH-40)
    text(screen,str(score),18,WIDTH/2,10)
    healthpoint(screen,int(player.health),25,WIDTH-20,10)
    pygame.display.update()

pygame.quit()