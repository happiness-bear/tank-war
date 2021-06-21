import pygame

class Home:
    """
    家
    """

    def __init__(self,aigame):
        #初始化
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()

        #加载墙的图像并获得其外接矩形
        self.image=pygame.image.load('image\\home.png')
        self.rect=self.image.get_rect()

        #将home放在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom


    def biltme(self):
        """
        在指定位置绘制home
        """
        self.screen.blit(self.image,self.rect)

