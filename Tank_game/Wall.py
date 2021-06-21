import pygame
from pygame.sprite import Sprite




class Brick(Sprite):
    """
    砖块
    """

    def __init__(self):
        #调用父类Sprite的初始化方法
        super().__init__()

        #加载墙的图像并获得其外接矩形
        self.image=pygame.image.load('image\\brick.png')
        self.rect=self.image.get_rect()


class Iron(Sprite):
    """
    铁块
    """

    def __init__(self):
        #调用父类Sprite的初始化方法
        super().__init__()

        #加载墙的图像并获得其外接矩形
        self.image=pygame.image.load('image\\iron.png')
        self.rect=self.image.get_rect()


class Map:
    """
    砖块与铁块的地理分布
    """
    
    def __init__(self,ai_game):
        #初始化
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #创建两个组来容纳砖块，铁块
        self.Brick_Group=pygame.sprite.Group()
        self.Iron_Group=pygame.sprite.Group()

        #初始化几个量
        self.brick=Brick()
        self.iron=Iron()

        #绘制墙块
        for i in range(30):
            #创建一个处于屏幕正中间的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =i*self.brick.rect.width,self.screen_rect.centery
            self.Brick_Group.add(self.brick)

        for i in range(30):
            #创建一个处于屏幕正中间的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =i*self.brick.rect.width,self.screen_rect.centery-24
            self.Brick_Group.add(self.brick)
        
        for i in range(30):
            #创建一个处于屏幕左侧的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =self.screen_rect.centerx/2,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)

        for i in range(30):
            #创建一个处于屏幕左侧的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =self.screen_rect.centerx/2+24,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)

        for i in range(30):
            #创建一个处于屏幕右侧的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =self.screen_rect.centerx*1.5,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)

        for i in range(30):
            #创建一个处于屏幕右侧的横排砖头墙
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =self.screen_rect.centerx*1.5-24,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)

        for x,y in [(360-48,720-24),(360-48,720-48),(360-48,720-72),(360-24,720-72),(360,720-72),(360+24,720-24),(360+24,720-48),(360+24,720-72)]:
            #用砖块将home围住
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =x,y
            self.Brick_Group.add(self.brick)

        for x,y in [(0,self.screen_rect.centery/2),(0,self.screen_rect.centery/2-24),
                    (24,self.screen_rect.centery/2),(24,self.screen_rect.centery/2-24),
                    (720-24,self.screen_rect.centery/2),(720-24,self.screen_rect.centery/2-24),
                    (720-48,self.screen_rect.centery/2),(720-48,self.screen_rect.centery/2-24)]:
            #创建铁块
            self.iron=Iron()
            self.iron.rect.left, self.iron.rect.top =x,y
            self.Iron_Group.add(self.iron)

        for i in range (9):
            #与铁块一起
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =48,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)

        for i in range (9):
            #与铁块一起
            self.brick=Brick()
            self.brick.rect.left, self.brick.rect.top =720-72,i*self.brick.rect.height
            self.Brick_Group.add(self.brick)


    def blitme(self):
        #画砖块
        for brick in self.Brick_Group:
            self.screen.blit(brick.image,brick.rect)
        #画铁块
        for iron in self.Iron_Group:
            self.screen.blit(iron.image,iron.rect)