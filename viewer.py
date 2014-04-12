

"""
Takes in sugarscape description to display in a pygame window.
"""
import numpy as np
import scipy.ndimage
import pygame
from pygame.locals import *
from random import randint


class Viewer:

    def __init__(self, pixel_width, pixel_height, grid_width, grid_height):
        # pixel size
        self.pw = pixel_width
        self.ph = pixel_height
        # number of grid spaces
        self.gw = grid_width
        self.gh = grid_height
        # init display
        self.surf  = pygame.display.set_mode((self.pw*self.gw,self.ph*self.gh))
        self.surf.fill((0,0,0))

        # dict to translate from sugarscape entities to colors
        self.trans_dict = dict()

    def display(self, field):
        # convert sugarscape field into color matrix
        #for w in range(self.gw):
        #    for h in range(self.gh):
        #        color = (randint(0,255), randint(0,255), randint(0,255))
        #        pos  = (self.pw*w,self.ph*h)
        #        size = (self.pw,self.ph)
        #        self.surf.fill(color, (pos, size))

        #arr = np.random.randint(0,255, (self.gh,self.gw,3))
        arr = field
        pygame.surfarray.blit_array(self.surf, arr)
        pygame.display.flip()
        
        #r = 0
        #g = 255
        #b = 0
        #c = r*(256**2) + g*(256) + b
        #arr = np.ones((10,10), dtype=np.int)*c
        #arr = np.random.randint(0,255*255*255*255, (10,10))
        #arr = scipy.ndimage.zoom(arr, self.pw, order=0)
        #pygame.surfarray.blit_array(self.surf, arr)
        #pygame.display.flip()




if __name__=='__main__':

    # test
    v = Viewer(1,1, 500,500)

    while True:
        v.display(None)

        

