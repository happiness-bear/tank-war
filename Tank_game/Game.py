import pygame
import sys
import pygame.display
import pygame.event
from Home import Home
from Wall import Map
from Tank import *
from Bullet import Bullet




class game:
    """
    游戏实例
    """

    def __init__(self):
        """
        初始化
        """
        pygame.init()
        #设置屏幕
        self.screen=pygame.display.set_mode((720,720))

        #设置标题
        pygame.display.set_caption("坦克大战")

        #加载各种类
        self.home=Home(self)
        self.map=Map(self)
        self.mytank=My_Tank(self)
        self.enemys=pygame.sprite.Group()
        self.group_list=[self.map.Brick_Group,self.map.Iron_Group]
        self.bullet=Bullet(self)
        self.bullets=pygame.sprite.Group()
        self.create_enemy()

        #游戏是否开始
        self.start=True 
        #子弹的数量限制
        self.num=3

    def draw_map(self):
        """
        画地图
        """
        self.map.blitme()


    def draw_home(self):
        """
        画home
        """
        self.home.biltme()

    
    def draw_my_tank(self):
        """
        画我方坦克
        """
        self.mytank.blit_my_tank()

    def game_over(self):
        if len(self.enemys)<=1:
            sys.exit()

    def fire(self):
        if len(self.bullets)<self.num:
            self.bullet=Bullet(self)
            self.bullets.add(self.bullet)
        pygame.sprite.groupcollide(self.bullets,self.map.Brick_Group,True,True)
        pygame.sprite.groupcollide(self.bullets,self.map.Iron_Group,True,False)
        pygame.sprite.groupcollide(self.bullets,self.enemys,True,True)


    def create_enemy(self):
        for position in [(0,0),(360-24,0),(720-48,0)]:
            enemy=Enemy_tank(position,self)
            self.enemys.add(enemy)



    def get_event(self):
        """
        获取事件
        """
        for event in pygame.event.get():
            #如果用鼠标点击了❌，那么就退出程序
            if event.type==pygame.QUIT:
                self.start=False
            #通过键盘控制坦克移动以及发射子弹
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                   self.mytank.direction='L'
                   self.mytank.stop=False
                elif event.key==pygame.K_d:
                    self.mytank.direction='R'
                    self.mytank.stop=False
                elif event.key==pygame.K_w:
                    self.mytank.direction='U'
                    self.mytank.stop=False
                elif event.key==pygame.K_s:
                    self.mytank.direction='D'
                    self.mytank.stop=False
                elif event.key==pygame.K_q:
                    sys.exit()
                elif event.key==pygame.K_SPACE:
                    self.fire()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_a or event.key==pygame.K_s or event.key==pygame.K_d \
                   or event.key==pygame.K_w:
                    self.mytank.stop=True

    
    def run_game(self):
        """
        运行游戏
        """
        #游戏主循环
        while True:
            if self.start:
                self.get_event()
                self.screen.fill((0,0,0))
                if self.mytank.life:
                    self.draw_my_tank()
                    self.mytank.move(self.group_list)
                for enemy in self.enemys:
                    enemy.blit_enemy_tank()
                    enemy.randomMove(self.group_list)
                for bullet in self.bullets:
                    bullet.Bullet_move()
                    bullet.blit_bullet()
                for bullet in self.bullets.copy():
                    if bullet.rect.top<=0 or bullet.rect.top>=720 or bullet.rect.right<=0 or bullet.rect.left>=720:
                        self.bullets.remove(bullet)
                #让最近绘制的屏幕可见
                self.draw_home()
                self.draw_map()
                self.game_over()
                pygame.display.flip()
            else:
                sys.exit()
    


if __name__=='__main__':
    """
    开始游戏
    """
    ai=game()
    ai.run_game()
