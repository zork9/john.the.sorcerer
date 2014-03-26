
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
from room1path import *
from masterdungeonkey1 import *

#
# This room fields the owl on the tree with nest
#

class MaproomSimple1:
    "Room 1 (simple stands for non-scrolling)"
    def __init__(self,playerx,playery):
        self.background = pygame.image.load('./pics/room-owl-2-640x480.bmp').convert()
	self.roompath = Room1Path(playerx, playery) 
	self.gameobjects = []
	self.masterdungeonkey1 = 0
	self.gameobjects.append(MasterDungeonKey1(0,0))

    def draw(self,screen,player):
        # draw bg
        screen.blit(self.background, (0, 0))
	for o in self.gameobjects:
		o.draw(screen)
	
    def pickup(self, player):###FIX for each room
	###print 'pickup1'
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
		### return id of the picked up item
                id = o.pickup(self)
                self.masterdungeonkey1 = 1
		print 'pickup'
		return id
        return 0

    def talkto(self, mousex, mousey):###FIX for each room
	###print 'talkto1'
        for o in self.gameobjects:
            if (o and o.collidecoord(mousex, mousey)):##FIX o.colidepickup
		### return id of the talkto item
                go = o.talkto(self)
		print 'talkto'
		return go 
        return None 

    def collide(self, xx,yy):
	for go in self.gameobjects:
		if (xx > go.x  and 
		xx < go.x+go.w and 
		yy > go.y and 
		yy < go.y + go.h):
		    ### print "collision in maproomsimple1 go=%s" % go
		    return go 
        return None

    def update(self, player):
	1    

    def isroomleftexit(self,game):
	if game.player.x  < 10: 
		return 1
	return 0

    def isroomrightexit(self,game):
	if game.player.x > 630:
		return 1
	return 0

    def exit(self, game):
	if self.isroomleftexit(game):
		###self.setxyfromdown()
		return 2 ### NOTE goto room number 2 (in game obj) 
	elif self.isroomrightexit(game):
		###self.setxyfromdown()
		return 3 ### NOTE goto room number 3 (in game obj) 
	return 0 

    def removeobject(self, o):
        for i in self.gameobjects:
	    if i!= None:
                if i == o:
                    i = None ###FIXME2

    def removeobjectlen(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
 
