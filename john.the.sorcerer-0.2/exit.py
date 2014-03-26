
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

class Exit(Gameobject):
    "Exit Game object"
    def __init__(self, xx,yy,ww,hh,name):
	Gameobject.__init__(self,xx,yy,ww,hh)
	# default width and height 
        self.w = ww 
        self.h = hh 
	self.name = name

    def draw(self, screen):
	1
 
    def drawstatic(self, screen):
	1 

    def drawininventory(self, screen,xx,yy):
	1
 
    def collide(self, room, player):
	if (player.x > self.x  and 
	player.x < self.x+self.w and 
	player.y > self.y and 
	player.y < self.y + self.h):
	    print "collision with Exit : %s" % self.name
	    return 1 
	else:
	    return 0 

    def collidecoord(self, xx, yy):
	if (xx > self.x  and 
	xx < self.x+self.w and 
	yy > self.y and 
	yy < self.y + self.h):
	    print "collision with Exit : %s" % self.name
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
        return None 


    def talk(self, screen):
	1

    def hitwithweapon(self,damage):
	1

    def fight(self,room,player):
	1
    
    def fightstatic(self,room,player):
	1
    
    def undomove(self):
	1
