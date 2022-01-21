import pygame
from pygame.locals import QUIT
from window import Window
import sys

class Main:
    def setWindow(self, dimensions, title):
        self.window = Window(dimensions, title)
    
    # def setConfig(self):
    #     print("b")

    def __init__(self):
        pygame.init()
        self.setWindow((800, 500), "MonUPoly")
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
        
    

    
a = Main()
a.run()