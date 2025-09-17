import pygame

print('setup start')
pygame.init()

window = pygame.display.set_mode(size = (600, 480))

print('Loop start')
while True:
    #check for all envents
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit() #close Window
            quit() #end pygame
