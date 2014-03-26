#!/usr/local/bin/python
# Copyright (C) Johan Ceuppens 2010
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

class Talktextlibrary:
    def __init__(self, font = None):
	self.index = 0
	self.max = 0
	self.list = []
	if font:
		self.font = font
	else:
        	self.font = pygame.font.SysFont("Times", 18)

    def addtext(self, s):
	self.list.append(s)
	self.max += 1

    def drawstatic(self, screen, xx, yy, index):
	if (self.index >= self.max):
            self.index = 0

	screen.blit(self.font.render(self.list[index], 6, (211,211,211)), (xx,yy))

    def draw(self, screen, xx, yy):
	if (self.index >= self.max):
            self.index = 0

	screen.blit(self.font.render(self.list[self.index], 6, (0,0,200)), (xx,yy))
	self.index += 1	
