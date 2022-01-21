import pygame
#from config import settings as s

class Window:
    def setDimensions(self, dimensions):
        self.getDisplay().set_mode(dimensions)
        self.dimensions = dimensions
    
    def setDisplay(self, display):
        self.display = display

    def getDisplay(self):
        return self.display

    def setTitle(self, text):
        self.getDisplay().set_caption(text)

    #Constructor
    def __init__ (self, dimensions, title):
        pygame.init()
        self.setDisplay(pygame.display)
        self.setDimensions(dimensions)
        self.setTitle(title)
    
        


'''
#print(sett.get("Fullscreen"))

#getting the dimensions 
width = sett.get("Screen_width")
height = sett.get("Screen_height")

screen = pygame.display.set_mode((width, height))

pygame.display.update()

loop = True

#main loop
while loop:
    for event in pygame.event.get():
        #exit handleing
        if event.type == pygame.QUIT:
             loop = False
'''
