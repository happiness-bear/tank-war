import pygame
import random
import pygame.sprite
from Bullet import Bullet

class Base_Tank(pygame.sprite.Sprite):
    """
    基础坦克父类
    """

    def __init__(self,ai_game):
        #调用父类Sprite的初始化方法
        super().__init__()

        #初始化
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #生命
        self.life=1

        #速度
        self.speed=8

        #初始方向
        self.direction='U'

        #子弹数量
        self.bullets_limit=1

        #等级
        self.level=1




class My_Tank(Base_Tank):
    """
    己方坦克
    """

    def __init__(self, ai_game):
         #调用父类Base_Tank的初始化方法
        super().__init__(ai_game)

        #生命
        self.life=3

        #是否停止移动
        self.stop=True

        #坦克的方向
        self.images = {
               'U': pygame.image.load('image\\my_tank_up.png'),
               'D': pygame.image.load('image\\my_tank_dowm.png'),
               'L': pygame.image.load('image\\my_tank_left.png'),
               'R': pygame.image.load('image\\my_tank_right.png')
              }

        #移动速度
        self.speed=1

        #加载坦克的图像并获得其外接矩形
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()

        #坦克的初始位置
        self.rect.left=360-96
        self.rect.top=720-48

    
    #def update_direction(self):
    #    """
    #    更新坦克的朝向
    #    """
    #    if self.direction == 'U':
    #        self.image = self.images[self.direction]
    #    elif self.direction == 'D':
    #        self.image = self.images[self.direction]
    #    elif self.direction == 'L':
    #        self.image = self.images[self.direction]
    #    elif self.direction == 'R':
    #        self.image = self.images[self.direction]

    def move(self,group_list):
        """
        坦克的移动
        """

        # 如果要移动的方向与当前坦克的朝向不同，则先调整朝向
        if self.direction=='U':
            self.image=self.images[self.direction]
            if self.rect.top>0 and not self.stop:
                self.rect.top-=self.speed
            else:
                self.stop=True
        elif self.direction == 'D':
            self.image=self.images[self.direction]
            if self.rect.top+self.rect.height<720 and not self.stop:
                self.rect.top+=self.speed
            else:
                self.stop=True
        elif self.direction == 'L':
            self.image=self.images[self.direction]
            if self.rect.left>0 and not self.stop:
                self.rect.left-=self.speed
            else:
                self.stop=True
        elif self.direction == 'R':
            self.image=self.images[self.direction]
            if self.rect.left+self.rect.width<720 and not self.stop:
                self.rect.left+=self.speed
            else:
                self.stop=True
        # 检测碰撞"砖墙"、"铁墙".
        for group in group_list:
            if pygame.sprite.spritecollide(self, group, False, None):
                self.stop=True
        

    

    
    def blit_my_tank(self):
        self.iamge=self.images[self.direction]
        self.screen.blit(self.image,self.rect)



class Enemy_tank(Base_Tank):
    """
    敌方坦克
    """

    def __init__(self,position, ai_game):
        super().__init__(ai_game)

        #是否停止移动
        self.stop=True

        #坦克的方向
        self.images = {
               'U': pygame.image.load('image\\enemy_tank_up.png'),
               'D': pygame.image.load('image\\enemy_tank_down.png'),
               'L': pygame.image.load('image\\enemy_tank_left.png'),
               'R': pygame.image.load('image\\enemy_tank_right.png')
              }

        #移动速度
        self.speed=10

        #初始方向
        self.direction=random.choice(['U','D','L','R'])

        #加载坦克的图像并获得其外接矩形
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()

        #初始位置
        self.rect.topleft=position

        #移动的步伐
        self.step=60

    def move(self,group_list):#,my_tank_group,brick_group,iron_group):
        """
        坦克的移动
        """
        if self.direction=='U':
            self.image=self.images[self.direction]
            if self.rect.top>0 and not self.stop:
                self.rect.top-=self.speed
                return
            else:
                self.stop=True
        elif self.direction == 'D':
            self.image=self.images[self.direction]
            if self.rect.top+self.rect.height<720 and not self.stop:
                self.rect.top+=self.speed
                return
            else:
                self.stop=True
        elif self.direction == 'L':
            self.image=self.images[self.direction]
            if self.rect.left>0 and not self.stop:
                self.rect.left-=self.speed
                return
            else:
                self.stop=True
        elif self.direction == 'R':
            self.image=self.images[self.direction]
            if self.rect.left+self.rect.width<720 and not self.stop:
                self.rect.left+=self.speed
                return
            else:
                self.stop=True
        # 检测碰撞"砖墙"、"铁墙".
        for group in group_list:
            if pygame.sprite.spritecollide(self, group, False, None):
                self.stop=True


    # 坦克随机移动
    def randomMove(self,group_list):
        if self.step < 0:
            self.direction = random.choice(['U','D','L','R'])
            self.step = 60
        else:
            self.move(group_list)
            self.step -= 1            
    

    def blit_enemy_tank(self):
        self.iamge=self.images[self.direction]
        self.screen.blit(self.image,self.rect)

    