
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

class Gameobject:
    "Game object"
    def __init__(self, xx,yy,ww,hh):
	self.x = xx 
        self.y = yy
	# default width and height 
        self.w = ww
        self.h = hh
        self.SCREENH = 640
        self.SCREENW = 480

	self.name = "Gameobject Base"

        ## dungeon statue as default picture
        ## self.image = pygame.image.load('./pics/dungeon-statue1-36x36.bmp').convert()
###        self.image = pygame.image.load('./pics/nopicture.bmp').convert()
###        self.image.set_colorkey((0,0,0)) 
        self.hitpoints = 1
        # NOTE : decrease 1 hitpoint with default sword
        self.hitf = self.hit1
        self.meter = None
        self.battlemode = None
        
    def draw(self, screen):   ###, room):
        ### screen.blit(self.image,(self.x+room.relativex,self.y+room.relativey))
        screen.blit(self.image,(self.x,self.y))
	    
	     
    def collidewithsword(self, room, player):
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0

    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
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

    def talk(self, screen, font):
	1			
	
