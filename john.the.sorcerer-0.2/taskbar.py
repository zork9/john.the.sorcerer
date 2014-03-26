
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
from taskbarbuttonhighlightwalkto import *
from taskbarbuttonhighlightlookat import *
from taskbarbuttonhighlightopen import *
from taskbarbuttonhighlightmove import *
from taskbarbuttonhighlightconsume import *
from taskbarbuttonhighlightpickup import *
from taskbarbuttonhighlightclose import *
from taskbarbuttonhighlightuse import *
from taskbarbuttonhighlighttalkto import *
from taskbarbuttonhighlightremove import *
from taskbarbuttonhighlightwear import *
from taskbarbuttonhighlightgive import *

class Taskbar:
    "Taskbar"
    def __init__(self, screen, font):
        self.screen = screen	
        self.font = font
        self.background = pygame.image.load('./pics/blank-purple.bmp').convert()
        self.background.set_colorkey((0,0,255)) 
       
	### taskbar widgets
	self.walkto = TaskbarButtonHighlightWalkTo(screen, font) 
	self.lookat = TaskbarButtonHighlightLookAt(screen, font) 
	self.open = TaskbarButtonHighlightOpen(screen, font) 
	self.move = TaskbarButtonHighlightMove(screen, font) 
	self.consume = TaskbarButtonHighlightConsume(screen, font) 
	self.pickup = TaskbarButtonHighlightPickUp(screen, font) 
	self.close = TaskbarButtonHighlightClose(screen, font) 
	self.use = TaskbarButtonHighlightUse(screen, font) 
	self.talkto = TaskbarButtonHighlightTalkTo(screen, font) 
	self.remove = TaskbarButtonHighlightRemove(screen, font) 
	self.wear = TaskbarButtonHighlightWear(screen, font) 
	self.give = TaskbarButtonHighlightGive(screen, font) 
 
    def collide(self,xx,yy):
	if (self.walkto.collide(xx,yy)):
		return (self.walkto, 1)
	if (self.lookat.collide(xx,yy)):
		return (self.lookat, 2)
	if (self.open.collide(xx,yy)):
		return (self.open, 3)
	if (self.move.collide(xx,yy)):
		return (self.move, 4)
	if (self.consume.collide(xx,yy)):
		return (self.consume, 5)
	if (self.pickup.collide(xx,yy)):
		return (self.pickup, 6)
	if (self.close.collide(xx,yy)):
		return (self.close, 7)
	if (self.use.collide(xx,yy)):
		return (self.use, 8)
	if (self.talkto.collide(xx,yy)):
		return (self.talkto, 9)
	if (self.remove.collide(xx,yy)):
		return (self.remove, 10)
	if (self.wear.collide(xx,yy)):
		return (self.wear, 11)
	if (self.give.collide(xx,yy)):
		return (self.give, 12)
	return None

    def highlight(self):
	if "highlight" in dir(self.walkto):	
		self.walkto.highlight()
	if "highlight" in dir(self.lookat):	
		self.lookat.highlight()
	if "highlight" in dir(self.open):	
		self.open.highlight()
	if "highlight" in dir(self.move):	
		self.move.highlight()
	if "highlight" in dir(self.consume):	
		self.consume.highlight()
	if "highlight" in dir(self.pickup):	
		self.pickup.highlight()
	if "highlight" in dir(self.close):	
		self.close.highlight()
	if "highlight" in dir(self.use):	
		self.use.highlight()
	if "highlight" in dir(self.talkto):	
		self.talkto.highlight()
	if "highlight" in dir(self.remove):	
		self.remove.highlight()
	if "highlight" in dir(self.wear):	
		self.wear.highlight()
	if "highlight" in dir(self.give):	
		self.give.highlight()

    def unhighlight(self):
	if "unhighlight" in dir(self.walkto):	
		self.walkto.unhighlight()
	if "unhighlight" in dir(self.lookat):	
		self.lookat.unhighlight()
	if "unhighlight" in dir(self.open):	
		self.open.unhighlight()
	if "unhighlight" in dir(self.move):	
		self.move.unhighlight()
	if "unhighlight" in dir(self.consume):	
		self.consume.unhighlight()
	if "unhighlight" in dir(self.pickup):	
		self.pickup.unhighlight()
	if "unhighlight" in dir(self.close):	
		self.close.unhighlight()
	if "unhighlight" in dir(self.use):	
		self.use.unhighlight()
	if "unhighlight" in dir(self.talkto):	
		self.talkto.unhighlight()
	if "unhighlight" in dir(self.remove):	
		self.remove.unhighlight()
	if "unhighlight" in dir(self.wear):	
		self.wear.unhighlight()
	if "unhighlight" in dir(self.give):	
		self.give.unhighlight()

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
