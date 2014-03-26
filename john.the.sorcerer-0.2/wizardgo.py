
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
from gameobject import *
from stateimagelibrary import *
from talktextlibrary import *

class WizardGO(Gameobject):
    "Wizard Game object"
    def __init__(self, xx,yy,ww,hh,name):
	Gameobject.__init__(self,xx,yy,ww,hh)
	# default width and height 
        self.w = ww 
        self.h = hh 
	self.name = name
      	self.stimlib = Stateimagelibrary()  
	self.image1 = pygame.image.load('./pics/nopicture.bmp').convert()
        self.image1.set_colorkey((0,0,0)) 
       	self.stimlib.addpicture(self.image1)
      	self.talktextlib = Talktextlibrary()  
	self.talktextlib.addtext("Nurks!") 
	self.talktextlib.addtext("BossNurks!") 

    def endoftalk(self):
	if self.talktextlib.index >= self.talktextlib.max:
		return 1
	else:
		return 0

    def draw(self, screen):
	self.stimlib.draw(screen, self.x, self.y)	
 
    def drawstatic(self, screen):
	self.stimlib.drawstatic(screen, self.x, self.y, 0)	
 
    def drawininventory(self, screen,xx,yy):
	self.stimlib.drawstatic(screen, xx, yy, 0)	
 
    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x > self.x  and 
	player.x < self.x+self.w and 
	player.y > self.y and 
	player.y < self.y + self.h):
	    print "collision with Dungeon Master Key"
	    return 1 
	else:
	    return 0 

    def collidecoord(self, xx, yy):
	if (xx > self.x  and 
	xx < self.x+self.w and 
	yy > self.y and 
	yy < self.y + self.h):
	    print "collision coord with DungeonMasterKey"
	    return 1 
	else:
	    return 0 ## for game self.talker

    def collidepickup(self, room, player):
        # FIX BUG
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y+self.h and 
	player.y-room.relativey < self.y+ self.h):
	    #print "pickup collision!"	
	    return 3 
	else:
	    return 0 
    
    def update(self,room,player):
	1

    def pickup(self, room):
        return 0

    def talkto(self, room):
        return self


    def talk(self, screen):
	self.talktextlib.draw(screen, self.x,self.y)	

    def talkstatic(self, screen, n):
	self.talktextlib.drawstatic(screen, self.x,self.y,n)	

    def fight(self,room,player):
	1
    
    def fightstatic(self,room,player):
	1
    
    def undomove(self):
	1
