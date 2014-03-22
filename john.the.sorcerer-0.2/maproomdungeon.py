
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
from time import *
from maproom import *

class MaproomDungeon(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.northwalls = []
        self.southwalls = []
        self.westwalls = []
        self.eastwalls= []
        self.gameobjects = []
        self.tileboxes = []
        self.pits = []
        
        self.automove = 0
        self.autodirection = "north"
        
    def addnorthwall(self, x,y):
        self.northwalls.append(MaproomNorthDungeonWall(x,y))

    def addsouthwall(self, x,y):
        self.southwalls.append(MaproomSouthDungeonWall(x,y))

    def addwestwall(self, x,y):
        self.westwalls.append(MaproomWestDungeonWall(x,y))

    def addeastwall(self, x,y):
        self.eastwalls.append(MaproomEastDungeonWall(x,y))
        
    def draw(self,screen):
	##print "x=%d" % self.relativex 
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for w in self.northwalls:
            w.draw(screen,self.relativex,self.relativey)
            
##        if self.automove:
##            print 'automove doing'
##            if self.autodirection == "north":
##                self.automovedown()
##            elif self.autodirection == "south":
##                self.automoveup()
##            elif self.autodirection == "west":
##                self.automoveright()
##            elif self.autodirection == "east":
##                self.automoveleft()
##
    def update(self,player):
        if self.automove:
            if player.mousex < player.x:
                self.automoveright()
            if player.mousex > player.x:
                self.automoveleft()
            if player.mousey < player.y:
                self.automovedown()
            if player.mousey > player.y:
                self.automoveup()

    def set_automove(self,player):
        if not player.highlightbase:
            return
        self.automove = 1
        # fall through for diagonal moving
##        if player.mousex < player.x:
##            self.autodirection = 'west'
##        if player.mousex > player.x:
##            self.autodirection = 'east'
##        if player.mousey < player.y:
##            self.autodirection = 'north'
##        if player.mousey > player.y:
##            self.autodirection = 'south'

    def automoveup(self):
	self.prevx = self.relativex
	self.prevy = self.relativey + 1
        self.relativey = self.relativey - 10

    def automovedown(self):
	self.prevx = self.relativex
	self.prevy = self.relativey - 1
        self.relativey = self.relativey + 10

    def automoveleft(self):
	self.prevx = self.relativex + 1
	self.prevy = self.relativey
        self.relativex = self.relativex - 10

    def automoveright(self):
	self.prevx = self.relativex - 1
	self.prevy = self.relativey
        self.relativex = self.relativex + 10
                
# NOTE player can be enemy 
    def collide(self, player):	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		return 2 # 1 kills game
	for i in self.northwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.southwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.westwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.eastwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.tileboxes:
		if i != None and i.collide(self,player):
			self.undomove()
			#player.circumvent(self)
	                # FIXME self.undomove()
			return 2 
	for i in self.pits:
		if i != None and i.collide(self,player):
			return 2
	return 0

    def collidewithenemy(self, enemy):
	for t in self.tileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
        return 0


