
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
from maproomdungeon import *
from room1path import *

class Maproom1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y,playerx,playery,aiengine):
        MaproomDungeon.__init__(self,x,y,640,480)
        self.background = pygame.image.load('./pics/room-owl-2-640x480.bmp').convert()
	self.roompath = Room1Path(playerx, playery) 
	self.masterdungeonkey1 = 0

    def draw(self,screen,player):
        # draw bg
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
##	for go in self.gameobjects:
##		go.blit	

    def pickup(self, player):###FIX for each room
	###print 'pickup1'
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
		### return the id of the picked up item 
                id = o.pickup(self)
                self.masterdungeonkey1 = 1
		print 'pickup'
		return id
        return 0
	


    def isroomleftexit(self,game):
	if game.player.x  < 10: 
		return 1
	return 0

    def isroomrightexit(self,game):
	if game.player.x > 630:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomleftexit(game):
		self.setxyfromdown()
		return 2 ### NOTE goto room number 2 (in game obj) 
	elif self.isroomrightexit(game):
		self.setxyfromdown()
		return 3 ### NOTE goto room number 3 (in game obj) 
	return 0 

    def talkto(self):#FIXME needs font
            print "talk to in maproom 6"
            ## return self.koboldwiz
            self.centaur1.talkcounter = 1
            return (self.centaur1,self.centaur2)
 
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single)
	return None


    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
