
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
from taskbarbutton import *

class TaskbarButtonHighlight(TaskbarButton):
    "Taskbar Button Highlight"
    def __init__(self, screen, font, xx, yy, filename):
	TaskbarButton.__init__(self, screen, font, xx, yy, filename)
	self.highlight = 0
	self.highlightedimage = self.image.copy()
	self.dither(self.highlightedimage)
		
    def draw(self):
	if self.highlight:
        	self.screen.blit(self.highlightedimage, (self.x, self.y))
	elif not self.highlight:
        	self.screen.blit(self.image, (self.x, self.y))
	else:
        	self.screen.blit(self.highlightedimage, (self.x, self.y))

    def click(self):
	1

    def highlight(self):
	self.highlight = 1

    def unhighlight(self):
	self.highlight = 0

    def dither(self, image):
	image.set_masks((0,0,100,100))

