
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
from maproomdungeon import *
from room1path import *

#
# This is the 
#

class MaproomSimple3:
    "Room 1 (simple stands for non-scrolling)"
    def __init__(self,playerx,playery):
        self.background = pygame.image.load('./pics/room-owl-2-640x480.bmp').convert()
	self.roompath = Room1Path(playerx, playery) 
	self.gameobjects = []

    def draw(self,screen,player):
        # draw bg
        screen.blit(self.background, (0, 0))
	
    def pickup(self, player):###FIX for each room
	###print 'pickup1'
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
                id = o.pickup(self)
                self.dungeonkey1 = 1
		print 'pickup'
		return id
        return 0

    def collide(self, player):
	1    

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

    def talkto(self):#FIXME needs font
            print "talk to in maproom 6"
            ## return self.koboldwiz
            self.centaur1.talkcounter = 1
            return (self.centaur1,self.centaur2)
 
