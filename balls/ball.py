import random
import pygame
colors = ['red','blue','green']
class Ball:
    def __init__(self,window,cooldown):
        """
        :param window: screen
        :param cooldown: controls how much time to wait between each teleport
        """
        self.win = window
        self.color = random.choice(colors)
        self.x = random.randint(2,18)*50
        self.y = random.randint(2,18)*50
        self.life_time = random.randint(50,100)
        self.cooldown = cooldown
        self.ready = cooldown
        #print(self.color)
        #print(self.x,self.y)
    def draw(self):
        """
        draws the ball
        """
        pygame.draw.circle(self.win, self.color, (self.x, self.y), 25)
    def teleport(self):
        """
        "deletes" the ball from where it was and changes its x and y, then draws in the new position
        """
        pygame.draw.circle(self.win, (255,255,255), (self.x, self.y), 25)
        self.x = random.randint(2,18)*50
        self.y = random.randint(2,18)*50
        self.draw()
        #print(self.x,self.y)

    def is_alive(self):
        """
        checks if needs to finish the thread
        """
        ret = self.life_time > 0
        if ret:
            self.life_time -= 1
        else:
            pygame.draw.circle(self.win, (255, 255, 255), (self.x, self.y), 25)
        return ret

    def try_tp(self):
        if self.ready > 0:
            self.ready -= 1
        else:
            self.ready = self.cooldown
            self.teleport()