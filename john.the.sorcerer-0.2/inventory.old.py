
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

class Inventory(object):
    def __init__(self,font):
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.listrow1 = []
        self.listrow2 = []
	self.ITEMWIDTH = 40
	self.ITEMHEIGHT = 40
	self.SCREENWIDTH = 640
	self.SCREENHEIGHT = 480
	self.ITEMMAX = 7
	#NOTE is in player classes :
	#self.listrow2.append(Inventorydefaultsword())
        #self.listrow1.append(Inventorybomb())
        self.font = font
        self.rectimage = pygame.image.load('./pics/rectinventory-36x36.bmp').convert()
	###        self.rectimage.set_colorkey((255,255,255))
        self.rectimage.set_colorkey((0,0,0))
        self.selectioncounter = 0 
        self.numberofkeys = 0
        self.keyimage = pygame.image.load('./pics/dungeonkey1.1-36x36.bmp').convert()
        self.keyimage.set_colorkey((0,0,255))
        self.numberofgold = 0
        self.goldcoinimage = pygame.image.load('./pics/goldcoin1.1-36x36.bmp').convert()
        self.goldcoinimage.set_colorkey((0,0,0))
        
    def setrow1(self, r):
        self.listrow1 = r

    def setrow2(self, r):
        self.listrow2 = r

    def addkey(self):
        self.numberofkeys += 1

    def draw(self,screen):

        screen.blit(self.background, (0, 0))
        screen.blit(self.font.render("Inventory", 6, (0,255,0)), (10,10))
        screen.blit(self.font.render("Inventory", 6, (0,0,255)), (12,12))

        screen.blit(self.font.render("Equipment", 6, (0,255,0)), (10,10+self.ITEMHEIGHT))
        screen.blit(self.font.render("Equipment", 6, (0,0,255)), (12,12+self.ITEMHEIGHT))

        screen.blit(self.font.render("Spells", 6, (0,255,0)), (10,10+self.ITEMHEIGHT*2))
        screen.blit(self.font.render("Spells", 6, (0,0,255)), (12,12+self.ITEMHEIGHT*2))

        screen.blit(self.font.render("Hit 'x' to go back to the game", 6, (255,0,0)), (12,self.SCREENHEIGHT - 20))

        pos = pygame.mouse.get_pos()
        mousex = pos[0]-18
        mousey = pos[1]-18

        self.selectioncounter = mousex % self.ITEMMAX

##        x = 80 + self.selectioncounter * self.ITEMWIDTH % self.ITEMMAX*self.ITEMWIDTH 
##	y = self.selectioncounter / self.ITEMMAX * self.ITEMWIDTH
	x = mousex ##% self.ITEMMAX*self.ITEMWIDTH 
	y = mousey ##self.selectioncounter / self.ITEMMAX * self.ITEMWIDTH
        
        for i in range(0,len(self.listrow1)):
            o = self.listrow1[i]
            if o:
                o.drawininventory(screen,80+40*(i%self.ITEMMAX),i/36)

        for i in range(0,len(self.listrow2)):
            o = self.listrow2[i]
            if o:
                o.drawininventory(screen,80+40*(i%self.ITEMMAX),i/36 + self.ITEMHEIGHT)

	
        
        screen.blit(self.keyimage,(10,320))
        screen.blit(self.font.render(" x %d" % self.numberofkeys, 6, (0,0,255)), (36,330))
        screen.blit(self.goldcoinimage,(110,320))
        screen.blit(self.font.render(" x %d" % self.numberofgold, 6, (0,0,255)), (136,330))
	### NOTE draw mouse rect pointer last
        self.drawrect(screen,x,y)

    def drawrect(self,screen,x,y):
        screen.blit(self.rectimage, (x, y))


    def moveleft(self):
        if self.selectioncounter > 0:
            self.selectioncounter -= 1

    def moveright(self):
        if self.selectioncounter < self.ITEMMAX * self.ITEMMAX:
            self.selectioncounter += 1

#    def setselection(self):
#        i = 
        
    def getitem(self,o):
        pos = pygame.mouse.get_pos()
        mousex = pos[0]
        mousey = pos[1]
        if mousex > 80 and mousey < self.ITEMHEIGHT and (mousex - 80) / self.ITEMWIDTH <= len(self.listrow1) and len(self.listrow1) != 0: 
                print '1st mousex=%d mousey=%d' % (mousex,mousey)
                
                o = self.listrow1[(mousex-80) / self.ITEMWIDTH]
                if o:
            	    return o
        if mousex > 80 and mousey > self.ITEMHEIGHT and mousey <= self.ITEMHEIGHT*2 and (mousex-80) / self.ITEMWIDTH < len(self.listrow2) and len(self.listrow2) != 0: 
                print '2nd mousex=%d mousey=%d' % (mousex,mousey)
                o = self.listrow2[(mousex-80) / self.ITEMWIDTH]
                if o:
            	    return o
##	if self.ITEMMAX > self.selectioncounter:
##                if len(self.listrow1) > self.selectioncounter:
##                    o = self.listrow1[self.selectioncounter]
##                    if o:
##            		return o

        return None

    def additem(self,o):
	### FIXME
        self.listrow1.append(o)
