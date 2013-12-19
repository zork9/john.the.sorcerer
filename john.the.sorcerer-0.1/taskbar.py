
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

class Taskbar:
    "Taskbar"
    def __init__(self, screen, font):
        self.screen = screen	
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.background.set_colorkey((0,0,255)) 
        self.leftbg = pygame.image.load('./pics/taskbar-left-actions-3.bmp').convert()
        self.leftbg.set_colorkey((0,0,255)) 
        
    def draw(self):
        self.screen.blit(self.background, (0, 400))
        self.screen.blit(self.leftbg, (0, 380))
