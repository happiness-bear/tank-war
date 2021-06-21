import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    子弹
    """

    def __init__(self,ai_game):
        #调用父类Sprite的初始化方法
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #子弹可能的发射方向
        self.images = {
                       'U': pygame.image.load('image\\bullet_up.png'),
                       'D': pygame.image.load('image\\bullet_down.png'),
                       'L': pygame.image.load('image\\bullet_left.png'),
                       'R': pygame.image.load('image\\bullet_right.png')
                      }
        
        #子弹的方向应与坦克一致
        self.direction=ai_game.mytank.direction

        #加载子弹的图像并获得其外接矩形
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()

        #子弹的速度
        self.speed=20
        #子弹是否存在
        self.life=True

        # 根据坦克方向，生成子弹位置
        if self.direction == 'U':
            self.image=self.images[self.direction]
            self.rect.left = ai_game.mytank.rect.left + ai_game.mytank.rect.width/2 - self.rect.width/2
            self.rect.top = ai_game.mytank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.image=self.images[self.direction]
            self.rect.left = ai_game.mytank.rect.left + ai_game.mytank.rect.width/2 - self.rect.width/2
            self.rect.top = ai_game.mytank.rect.top + ai_game.mytank.rect.height
        elif self.direction == 'L':
            self.image=self.images[self.direction]
            self.rect.left = ai_game.mytank.rect.left - self.rect.width/2 - self.rect.width/2
            self.rect.top = ai_game.mytank.rect.top + ai_game.mytank.rect.height/2 - self.rect.width/2
        elif self.direction == 'R':
            self.image=self.images[self.direction]
            self.rect.left = ai_game.mytank.rect.left + ai_game.mytank.rect.width
            self.rect.top = ai_game.mytank.rect.top + ai_game.mytank.rect.height/2 - self.rect.width/2

    def Bullet_move(self):
        #子弹移动
        if self.direction == 'U':
            self.rect.top-=self.speed
        elif self.direction == 'D':
            self.rect.top+=self.speed
        elif self.direction == 'L':
            self.rect.left-=self.speed
        elif self.direction == 'R':
            self.rect.left+=self.speed

        

    def blit_bullet(self):
        self.screen.blit(self.image,self.rect)