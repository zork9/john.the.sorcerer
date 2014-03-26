#!/usr/local/bin/python
# Copyright (C) Johan Ceupens 2012-2014
# Copyright (C) Werner Van Belle 2013-2014
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

from maproomsimple1 import *
from maproomsimple2 import *
from maproomsimple3 import *
from inventory import *
from player import *

from taskbar import *

class JohnTheSorcererMain:
    "Main"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((640, 480))
        font = pygame.font.SysFont("Times", 14)
        font2 = pygame.font.SysFont("Vera", 28)
        font3 = pygame.font.SysFont("Courier", 10)
        gameover = 0
	self.displayeditem = None        
        blankimage = pygame.image.load('./pics/blank-purple.bmp').convert()
        titleimage = pygame.image.load('./pics/titlescreen.bmp').convert()
        self.x = 0
        self.y = 0

        while gameover == 0:
            pygame.display.update()
            screen.blit(titleimage, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1
                    
        screen.blit(blankimage, (0,0))

	###self.player = Player(550,340,-1)
	self.player = Player(100,200,1)
	self.player2 = Player(550,340,-1) ### FIXME delete
	self.aiengine = None
	self.taskbarmode = None
        ###self.room = MaproomSimple1(0,0,550,430,self.aiengine)
        self.room = MaproomSimple1(550,430)
	self.roomnumber = 1
	self.shortest_path_nodes = []
                
        self.inventoryitem = None
        self.inventorydungeonmasterkey1 = None
        self.inventorykey1 = None
        self.inventoryrubysword = None
        
        self.taskbar = Taskbar(screen,font)
        self.talkerlist = [] 

        self.position1stx = 0
        self.position1sty = 0
        self.position2ndx = 0
        self.position2ndy = 0
        self.positionmovex = 0
        self.positionmovey = 0        

        pygame.key.set_repeat(1,1)
        gameover = 0
        while gameover == 0:
                       
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ##FIXME righclick start ->
                    if pygame.mouse.get_pressed()[2]:
                        
                        # take room coords of mouse
                        mousepos = pygame.mouse.get_pos()
                        self.player.mousex = mousepos[0]-self.room.relativex
                        self.player.mousey = mousepos[1]-self.room.relativey
                        if self.player2:
                            self.player2.mousex = mousepos[0]-self.room.relativex
                            self.player2.mousey = mousepos[1]-self.room.relativey
                        
                        if self.room.automove == 0:
                            self.room.set_automove(self.player)
                            if self.player2:
                                self.room.set_automove(self.player2)
                        elif self.room.automove == 1:
                            self.room.automove = 0
                        break
                            
                    position1 = pygame.mouse.get_pos()
                    self.position1stx = position1[0]
                    self.position1sty = position1[1]

                    if self.collidewithclick(self.player,self.room,self.position1stx,self.position1sty,50,50):
                        self.player.highlight()
                        self.taskbar.highlight()
                    else:
                        if pygame.mouse.get_pressed()[0]:
                            self.player.unhighlight()

                if event.type == pygame.MOUSEBUTTONUP and self.taskbarmode and self.taskbarmode[1] == 1:
			### 1 : walkto button clicked
			self.player.changeorientation(self.position2ndx,self.position2ndy)
			self.shortest_path_nodes = self.room.roompath.find_path(self.position1stx, self.position1sty)
			self.taskbarmode = None	

                if event.type == pygame.MOUSEBUTTONUP and self.taskbarmode and self.taskbarmode[1] == 6 and self.displayeditem:
			### 6 : pickup button clicked
			self.player.changeorientation(self.position2ndx,self.position2ndy)
			self.shortest_path_nodes = self.room.roompath.find_path(self.position1stx, self.position1sty)
			self.taskbarmode = None	

                if event.type == pygame.MOUSEBUTTONUP and self.taskbarmode and self.taskbarmode[1] == 9 and self.displayeditem:
			### 9 : talkto button clicked
			self.player.changeorientation(self.position2ndx,self.position2ndy)
			self.shortest_path_nodes = self.room.roompath.find_path(self.position1stx, self.position1sty)
			self.taskbarmode = None
		    	talkgo = self.room.talkto(self.position1stx,self.position1sty)
		    	#print "talkid=%s" % talkid
		    	if talkgo:
			### roomnumber 1 talkto items
	###		if self.roomnumber == 1:
###			if talkgo.name == "Master Dungeon Key":
				self.talkerlist.append(talkgo) 
				print "self.talkerlist=%s" % self.talkerlist[0]

                elif event.type == pygame.MOUSEBUTTONUP:

                    position2 = pygame.mouse.get_pos()
                    self.position2ndx = position2[0]
                    self.position2ndy = position2[1]
                   
			### NOTE, collide on taskbar button widgets 
	    	    self.taskbarmode = self.taskbar.collide(position2[0], position2[1])
		    if (self.taskbarmode != None and self.taskbarmode[0] != None):	
			print "clicked on %s" % self.taskbarmode[0]
			if (self.taskbarmode[1] == 1):
				### 1 : walkto button clicked
				1
			elif (self.taskbarmode[1] == 6):
				### 6 : pickup button clicked
				1
			elif (self.taskbarmode[1] == 9):
				### 9 : talkto button clicked
				1
           			 
                    self.position1stx = 0
                    self.position1sty = 0
                    self.position2ndx = 0
                    self.position2ndy = 0
                    self.positionmovex = 0
                    self.positionmovey = 0

		                    
                    
                if event.type == pygame.MOUSEMOTION:
                    positionmove = pygame.mouse.get_pos()
                    self.positionmovex = positionmove[0]-self.position1stx
                    self.positionmovey = positionmove[1]-self.position1sty
                    #print 'pos=%d' % positionmove[0]

		    
                    
                    ##FIXME righclick end
                    self.position1stx = 0
                    self.position1sty = 0
                    self.position2ndx = 0
                    self.position2ndy = 0
                    self.positionmovex = 0
                    self.positionmovey = 0


		    ### set display name of gameobject last hovered over
		    ### print "ROOM=%s" % self.room
		    go = self.room.collide(positionmove[0], positionmove[1])
		    if go:
			self.displayeditem = go
                    else:
			self.displayeditem = None
 
                elif event.type == KEYDOWN:
                    if event.key == K_i:
                        flag = 0
                        inventory = Inventory(font3)
    
                        if self.inventorykey1 == 1:
                            inventory.addkey()
			if self.inventorydungeonmasterkey1 == 1:
                       		inventory.additem(MasterDungeonKey1(0,0))
			while flag == 0:#NOTE1
                            pygame.key.set_repeat(1000,1000)
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        inventory.moveleft()
                                    elif event.key == K_RIGHT:
                                        inventory.moveright()
                                    elif event.key == K_x:
                                        self.inventoryitem = inventory.getitem(self.inventoryitem)
                                        pygame.key.set_repeat(1,1)
                                        flag = 1


                                inventory.draw(screen)
                                pygame.display.update()
            
	    pickupgo = self.room.pickup(self.player)
	    if pickupgo:
		### roomnumber 1 pickup items
		###if self.roomnumber == 1 or self.roomnumber == 1.1:###NOTE
		if pickupgo.name == "Master Dungeon Key": 
		    self.inventorydungeonmasterkey1 = 1
		    self.room.removeobjectlen(pickupgo)

            self.room.update(self.player)
            self.room.draw(screen,self.player) 
            self.player.drawstatic(screen)

	    ### automove
	    ### FIXME if (len(self.shortest_path_nodes) > 0):
	    if (self.shortest_path_nodes and len(self.shortest_path_nodes) > 0):
		self.pathnode = self.shortest_path_nodes[0]
	    	if (self.player.x == self.pathnode.x and self.player.y == self.pathnode.y): 
			self.shortest_path_nodes.pop(0)
	        else:
			if (self.player.x < self.pathnode.x):
				self.player.x += 1		
			elif (self.player.x > self.pathnode.x):
				self.player.x -= 1		
			if (self.player.y < self.pathnode.y):
				self.player.y += 1		
			elif (self.player.y > self.pathnode.y):
				self.player.y -= 1		


            if self.player2:
                self.player2.drawstatic(screen)

            for o in self.room.gameobjects:
                if o:
                    if randint(0,1) == 0:
                        o.fight(self.room,self.player)
                    	if o.hitpoints <= 0:
                        	self.room.removeobject(o)
                    elif self.player2 and randint(0,1) == 0:
                        o.fight(self.room,self.player2)
                    	if o.hitpoints <= 0:
                        	self.room.removeobject(o)
	    ###FIXME sleep(0.2)
            # fight for enemies
            # remove dead game objects

	    ### Set self.player hitpoints in life bar

            for o in self.room.gameobjects:
                if o:
                    o.fight(self.room,self.player)
                    if o.hitpoints <= 0:
                        self.room.removeobject(o)

            if self.talkerlist != None:
                for o in self.talkerlist:
                    if o != None:
                        o.talk(screen)

            if self.position1stx != 0 or self.position1sty != 0:
                pygame.draw.rect(screen, (255,0,0), ((self.position1stx,self.position1sty),(self.positionmovex,self.positionmovey)),1)
                # collide with selection rectangle, this method is also in MOUSEBUTTONUP
                if self.collidewithrect(self.player,self.room,self.position1stx,self.position1sty,self.positionmovex,self.positionmovey):
                    print 'highlight'
                    self.player.highlight()
                    self.taskbar.highlight()
                if self.player2:
                    if self.collidewithrect(self.player2,self.room,self.position1stx,self.position1sty,self.positionmovex,self.positionmovey):
                        print 'highlight'
                        self.player2.highlight()
                        # FIXME self.player 2
                        self.taskbar.highlight()

            position = pygame.mouse.get_pos()
                
            self.taskbar.draw()
	    if self.displayeditem:
	    	screen.blit(font2.render(self.displayeditem.name, 16, (255,255,255)), (250,390))

            pygame.display.update()
            screen.blit(blankimage, (0,0))
            self.roomnumber = self.room.exit(self)
            self.chooseroom(self.roomnumber,font)


    def sethitf(self, hitf):
        for i in self.room.gameobjects:
            i.hitf = hitf

    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    def chooseroom(self, roomnumber,font):
        if (roomnumber == 0):
            return
        # enter room 1  
        elif (roomnumber == 1):
            self.talker = None
            self.room = MaproomSimple1(0,0)
        # enter room 1 and change player coords to right of room (coming from the left)  
        elif (roomnumber == 1.1):
            self.talker = None
            self.room = MaproomSimple1(0,0)
	    self.player.x = 550
	    self.player.y = 340 
        elif (roomnumber == 2):
            self.talker = None
            self.room = MaproomSimple2(0,0)
        elif (roomnumber == 3):
            self.talker = None
            self.room = MaproomSimple3(0,0)

        # set sword parameters
        if self.inventoryrubysword:
            self.sethitf(self.room.gameobjects.hit2)

        # collide with selection rectangle
    def collidewithrect(self, player,room,xx,yy,ww,hh):
            # FIX BUG
            #print 'rect x=%d y=%d self.player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
        #print 'rect x=%d y=%d self.player x=%d y=%d' % (xx,yy,player.x,player.y)
        if (player.x > xx  and 
            player.x < xx+ww and 
            player.y > yy and 
            player.y < yy + hh):
	    print "collision with Rect!"
            return 1 
        else:
            return 0

    def collidewithclick(self, player,room,xx,yy,ww,hh):
            # FIX BUG
            #print 'rect x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
        #print 'rect x=%d y=%d self.player x=%d y=%d' % (xx,yy,self.player.x,self.player.y)
        if (player.x+player.w > xx  and 
            player.x < xx+ww and 
            player.y+player.h > yy and 
            player.y < yy + hh):
	    print "collision with ClickRect! (highlight)"
            return 1 
        else:
            return 0 

            
if __name__ == "__main__":
    foo = JohnTheSorcererMain()



