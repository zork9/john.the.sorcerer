
# Copyright (C) Johan Ceuppens 2010-2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from stateimagelibrary import *
from playerbase import *
from rng import *

class Player(PlayerBase):
    "Player"
    def __init__(self, startx, starty, orientation):
	PlayerBase.__init__(self)        
        self.stimlibright = Stateimagelibrary()
        self.image1 = pygame.image.load('./pics/simon-right-1-48x100.bmp').convert()
        self.image1.set_colorkey((0,0,0))
	self.stimlibright.addpicture(self.image1)

        self.stimlibrighthighlight = Stateimagelibrary()
	self.highlightedimage1 = self.image1.copy()
	self.dither(self.highlightedimage1) 
	self.stimlibrighthighlight.addpicture(self.highlightedimage1)
	self.highlight = 0 

        self.stimlibleft = Stateimagelibrary()
        self.image2 = pygame.image.load('./pics/simon-left-1-48x100.bmp').convert()
        self.image2.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(self.image2)

	self.x = startx
	self.y = starty 
	self.w = 48 
	self.h = 100 
        self.hitpoints = 50
	self.orientation = orientation ### -1 == left, 1 == right 

    def dither(self, image):
	image.set_masks((0,0,100,100))

    def changeorientation(self, xx,yy):
	if xx < self.x:
		self.orientation = -1
	elif xx > self.x:
		self.orientation = 1
	else:
		self.orientation = -1

    def draw(self, screen):
	if self.orientation == -1:
		self.stimlibleft.draw(screen, self.x, self.y)	
	elif self.orientation == 1:
		if self.highlight:
			self.stimlibrighthighlight.draw(screen, self.x, self.y)	
	else:
		self.stimlibleft.draw(screen, self.x, self.y)	
 
    def drawstatic(self, screen):
	self.stimlibright.drawstatic(screen, self.x, self.y, 0)	
 
    def pickup(self,room):
        n = room.pickup(self)
	return n

    def highlight(self):
	self.highlight = 1	

    def unhighlight(self):
	self.highlight = 0	
