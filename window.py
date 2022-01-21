import pygame
from config import settings as sett

print(sett.get("Fullscreen"))

#getting the dimensions 
width = sett.get("Screen_width")
height = sett.get("Screen_height")

screen = pygame.display.set_mode((width, height))

pygame.display.flip()

loop = True

#main loop
while loop:
    for event in pygame.event.get():
        #exit handleing
        if event.type == pygame.QUIT:
             loop = False
