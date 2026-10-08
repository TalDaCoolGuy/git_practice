import threading
import pygame

from ball import Ball


def ball_control(bal,):
    """
    :param bal: ball class
    controls the ball and says when finish the thread
    """
    bal.draw()
    alive = True
    while alive:
        pygame.time.delay(60)
        bal.try_tp()
        alive = bal.is_alive()
    print(f"remaining balls: {threading.active_count() - 2}") #-1 because the "if __name__ == '__main__':" is a thread and another -1 because it didnt really finish

if __name__ == '__main__':
    win = pygame.display.set_mode((1000, 1000))
    while True:
        balls = input("how manny balls do u need?")
        if balls.isdigit():
            for i in range(int(balls)):
                ball = Ball(win,5)
                threading.Thread(target=ball_control,args=(ball,),daemon=True).start()
            break
        continue

    #the pygame activation stuff
    running = True
    pygame.init()
    win.fill((255, 255, 255))
    while running:
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        if threading.active_count() - 1 <= 0:
            running = False
