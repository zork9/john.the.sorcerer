
# Copyright (C) Johan Ceuppens 2010-2013 
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

class TaskbarButton:
    "Taskbar Button"
    def __init__(self, screen, font, xx, yy, filename):
        self.screen = screen	
        self.font = font
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0,0,0)) 
       	self.x = xx
	self.y = yy
	self.w = 60
	self.h = 40

    def collide(self,xx,yy):
	if (xx > self.x and xx < self.x + self.w and yy > self.y and yy < self.y + self.h):
		return 1
	else:
		return None 
 
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def click(self):
	print "sorcerer error : subclass responsability"
