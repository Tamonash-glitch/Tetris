import pygame,sys
pygame.init()
from game import Game

width=300
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Tetris")

clock=pygame.time.Clock()

game=Game()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                game.move_left()
            if event.key==pygame.K_RIGHT:
                game.move_right()
            if event.key==pygame.K_DOWN:
                game.move_down()
    screen.fill((44,44,127))
    game.draw(screen)


    pygame.display.update()
    clock.tick(60)