
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
from taskbarbuttonwalkto import *
from taskbarbuttonlookat import *
from taskbarbuttonopen import *
from taskbarbuttonmove import *
from taskbarbuttonconsume import *
from taskbarbuttonpickup import *
from taskbarbuttonclose import *
from taskbarbuttonuse import *
from taskbarbuttontalkto import *
from taskbarbuttonremove import *
from taskbarbuttonwear import *
from taskbarbuttongive import *

class Taskbar:
    "Taskbar"
    def __init__(self, screen, font):
        self.screen = screen	
        self.font = font
        self.background = pygame.image.load('./pics/blank-purple.bmp').convert()
        self.background.set_colorkey((0,0,255)) 
       
	### taskbar widgets
	self.walkto = TaskbarButtonWalkTo(screen, font) 
	self.lookat = TaskbarButtonLookAt(screen, font) 
	self.open = TaskbarButtonOpen(screen, font) 
	self.move = TaskbarButtonMove(screen, font) 
	self.consume = TaskbarButtonConsume(screen, font) 
	self.pickup = TaskbarButtonPickUp(screen, font) 
	self.close = TaskbarButtonClose(screen, font) 
	self.use = TaskbarButtonUse(screen, font) 
	self.talkto = TaskbarButtonTalkTo(screen, font) 
	self.remove = TaskbarButtonRemove(screen, font) 
	self.wear = TaskbarButtonWear(screen, font) 
	self.give = TaskbarButtonGive(screen, font) 
 
    def collide(self,xx,yy):
	if (self.walkto.collide(xx,yy)):
		return self.walkto
	if (self.lookat.collide(xx,yy)):
		return self.lookat
	if (self.open.collide(xx,yy)):
		return self.open
	if (self.move.collide(xx,yy)):
		return self.move
	if (self.consume.collide(xx,yy)):
		return self.consume
	if (self.pickup.collide(xx,yy)):
		return self.pickup
	if (self.close.collide(xx,yy)):
		return self.close
	if (self.use.collide(xx,yy)):
		return self.use
	if (self.talkto.collide(xx,yy)):
		return self.talkto
	if (self.remove.collide(xx,yy)):
		return self.remove
	if (self.wear.collide(xx,yy)):
		return self.wear
	if (self.give.collide(xx,yy)):
		return self.give
	return None



    def draw(self):
        self.screen.blit(self.background, (0, 310))
	self.walkto.draw()
	self.lookat.draw()
	self.open.draw()
	self.move.draw()
	self.consume.draw()
	self.pickup.draw()
	self.close.draw()
	self.use.draw()
	self.talkto.draw()
	self.remove.draw()
	self.wear.draw()
	self.give.draw()
