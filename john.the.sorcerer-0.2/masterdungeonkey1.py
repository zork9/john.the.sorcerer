
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

class MasterDungeonKey1(Gameobject):
    "DungeoMasterKey Game object"
    def __init__(self, xx,yy):
	Gameobject.__init__(self,xx,yy,48,48)
	# default width and height 
        self.w = 48
        self.h = 48
	self.name = "Master Dungeon Key"
      	self.stimlib = Stateimagelibrary()  
	self.image1 = pygame.image.load('./pics/key1-48x48.bmp').convert()
        self.image1.set_colorkey((0,0,0)) 
       	self.stimlib.addpicture(self.image1)
      	self.talktextlib = Talktextlibrary()  
	self.talktextlib.addtext("The key says nothing") 
###    def draw(self, screen, room):
###        screen.blit(self.image,(self.x+room.relativex,self.y+room.relativey))

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
	    print "collision with DungeonMasterKey"
	    return 1 
	else:
	    return 0 ## for game self.talker

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
    
    def collideobjectX(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.x > i.x  and 
		    self.x < i.x+i.w):
	            return 1 
	return 0

    def collideobjectY(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.y > i.y  and 
		    self.y < i.y+i.h):
	            return 1 
	return 0
 
    def collideobjectXY(self, room):
	for i in room.gameobjects:
	    if i:		
	        if (self.x > i.x  and 
	 	    self.x < i.x+i.w and 
	            self.y > i.y and 
	            self.y < i.y+i.h):
	            return 1 
	return 0 
    
    def update(self,room,player):
	1

    def pickup(self, room):
        return 0

    def talkto(self, room):
        return self


    def talk(self, screen):
	self.talktextlib.draw(screen, self.x,self.y)	

    def hit1(self):## NOTE decreases hitpoints
        self.hitpoints -= 1
        return self.hitpoints

    def hit2(self):## NOTE decreases hitpoints
        self.hitpoints -= 2
        return self.hitpoints

    def hitwithweapon(self,damage):
	if damage > 0:
            print 'enemy is hit!'
        self.hitpoints -= damage
        self.battlemode = 1
        if self.meter:
            self.meter.index -= damage

    def fight(self,room,player):
	1
    
    def fightstatic(self,room,player):
	1
    
    def undomove(self):
	1
