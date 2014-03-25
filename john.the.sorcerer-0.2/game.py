#!/usr/local/bin/python
# Copyright (C) Johan Ceupens 2013
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
from maproom1 import *
from inventory import *
from player import *
### from maproom2 import *

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

	###self.player = Player(550,340)
	self.player = Player(100,200)
	self.player2 = Player(550,340) ### FIXME delete
	self.aiengine = None
	self.taskbarmode = None
        ###self.room = MaproomSimple1(0,0,550,430,self.aiengine)
        self.room = MaproomSimple1(550,430)
	self.shortest_path_nodes = []
                
        self.inventoryitem = None
        self.inventorymasterkey = None
        self.inventorykey1 = None
        self.inventorykey2 = None
        self.inventoryrubysword = None
        
        self.taskbar = Taskbar(screen,font)
        self.talkerlist = None

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
                            1###self.player.unhighlight()

                if event.type == pygame.MOUSEBUTTONUP:

                    position2 = pygame.mouse.get_pos()
                    self.position2ndx = position2[0]
                    self.position2ndy = position2[1]
                   
			### NOTE, collide on taskbar button widgets 
	    	    self.taskbarmode = self.taskbar.collide(position2[0], position2[1])
		    if (self.taskbarmode != None and self.taskbarmode[0] != None):	
			print "clicked on %s" % self.taskbarmode[0]
			if (self.taskbarmode[1] == 4):
				self.shortest_path_nodes = self.room.roompath.find_path(self.position1stx, self.position1sty)
           			 
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
                    
                elif event.type == KEYDOWN:
            	    
                    # self.player 1 key controls
                    self.player.draw(screen)
                    if self.player2:
                        self.player2.draw(screen)
                    if event.key == K_x:
                        if self.room.collide(self.player) == 2:
                            self.talkerlist = self.room.talkto() # FIX
                        if self.player2:
                            if self.room.collide(self.player2) == 2:
                                self.talkerlist = self.room.talkto()
                                print "self.talker=%s" % self.talkerlist[1]
			####if self.talkerlist == None:
                        #id = self.player.pickup(self.room)
			#if id == 3:
		        #       	self.taskbar.setdungeonkey1()
			#if id == 5:
		        #       	self.taskbar.setrubysword()
			#	self.player.setrubysword()
                    elif event.key == K_z:
                        self.player.fight(self.room)
                        if self.player2:
                            self.player2.fight(self.room)  
                    elif event.key == K_UP:
                        self.room.movedown()    
                    elif event.key == K_DOWN:
                        self.room.moveup()    
                    elif event.key == K_LEFT:
                        self.room.moveright()    
                    elif event.key == K_RIGHT:
                        self.room.moveleft()    
                    elif event.key == K_SPACE:
                        self.room.gameobjects.append(Bomb(self.player.x-self.room.relativex,self.player.y-self.room.relativey))
    
                    elif event.key == K_i:
#                        self.level.gameover = 1
                      #FIXME  pygame.event.flush()
                        flag = 0
                        inventory = Inventory(font3)
    
                        if self.inventorykey1 == 1:
                            inventory.addkey()
		
			##if Scrollinvisibility(0,0,0,0,"1","1").readkeys(None):
                        ##    inventory.additem(Inventoryscrollinvisibility())

			if self.inventorymasterkey == 1:
                       		1###FIX for key in inventory.additem(Inventorymasterkey())
                        if self.inventorykey1 == 1:
                       		1###FIX for key in inventory.additem(Inventorykey1())
                       	if self.inventorykey2 == 1:
                       		1###FIX for key in inventory
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
            
	    pickupid = self.room.pickup(self.player)
	    #print "pickup=%s" % pickupid
	    if pickupid:
		if pickupid == 1: # NOTE : masterkey id
		    self.inventorymasterkey = 1
		elif pickupid == 2: ## NOTE: dungeonentrance 2 id opens with key 1
                    if self.inventorykey1 == 1:
                        self.room.removeentrance2()
                elif pickupid == 3: # NOTE dungeon key 1 id
                    flag = 0
                    self.inventorykey1 = 1
                    pygame.key.set_repeat(1000,1000)
                    self.room.draw(screen,self.player) 
                    self.player.drawstatic(screen)
                    if self.player2:
                        self.player2.drawstatic(screen)
                    screen.blit(font2.render("You picked up a key. (Hit 'x' to continue)", 6, (0,0,200)), (100,100))
                    pygame.display.update()
                    while flag == 0:#NOTE1
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
                                    if event.key == K_x:
                                        pygame.key.set_repeat(1,1)
                                        flag = 1
                                     
                    self.inventorykey1 = 1
                elif pickupid == 4: # NOTE dungeon key 2 id
                    self.inventorykey2 = 1
                elif pickupid == 5: # NOTE ruby sword id
                    self.inventoryrubysword = 1
                    self.taskbar.setrubysword()

            if self.player2:
                pickupid = self.room.pickup(self.player2)
                #print "pickup=%s" % pickupid
                if pickupid:
                    if pickupid == 1: # NOTE : masterkey id
                        self.inventorymasterkey = 1
                    elif pickupid == 2: ## NOTE: dungeonentrance 2 id opens with key 1
                        if self.inventorykey1 == 1:
                            self.room.removeentrance2()
                    elif pickupid == 3: # NOTE dungeon key 1 id
                        flag = 0
                        self.inventorykey1 = 1
                        pygame.key.set_repeat(1000,1000)
                        self.room.draw(screen,self.player)
                        self.player.drawstatic(screen)
                        if self.player2:
                            self.player2.drawstatic(screen)
                        screen.blit(font2.render("You picked up a key. (Hit 'x' to continue)", 6, (0,0,200)), (100,100))
                        pygame.display.update()
                        while flag == 0:#NOTE1
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        return
                                    if event.type == MOUSEBUTTONDOWN:
                                        pygame.key.set_repeat(1,1)
                                        flag = 1
                                    elif event.type == KEYDOWN:
                                        if event.key == K_x:
                                            pygame.key.set_repeat(1,1)
                                            flag = 1
                                         
                        self.inventorykey1 = 1
                    elif pickupid == 4: # NOTE dungeon key 2 id
                        self.inventorykey2 = 1
                    elif pickupid == 5: # NOTE ruby sword id
                        self.inventoryrubysword = 1
                        self.taskbar.setrubysword()

	    # FIXME self.player 2
            if (self.room.collide(self.player) == 1 or self.player.hitpoints <= 0) or (self.player2 and self.player2.hitpoints <= 0): # NOTE: return 1 after self.player heartmeter runs out (self.player.hit)
                endingimage = pygame.image.load('./pics/endingscreen.bmp').convert()
                while gameover == 0:
                        pygame.display.update()
                        screen.blit(endingimage, (0,0))
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        return
                                elif event.type == KEYDOWN:
                                        gameover = 1
                                        return
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        gameover = 1
                                        return
            ###if self.room.collide(self.player) == 3:###Dungeon wall
                ##self.room.undomove()
            ###    self.room.removeentrance2()
            self.room.update(self.player)
            self.room.draw(screen,self.player) 
            self.player.drawstatic(screen)


	    ### automove
	    if (len(self.shortest_path_nodes) > 0):
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
	    sleep(0.2)
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
                        o.talk(screen,font)

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

            pygame.display.update()
            screen.blit(blankimage, (0,0))
            roomnumber = self.room.exit(self)
            self.chooseroom(roomnumber,font)


    def sethitf(self, hitf):
        for i in self.room.gameobjects:
            i.hitf = hitf

    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    def chooseroom(self, roomnumber,font):
        if (roomnumber == 0):
            return
        # NOTE: 1_X  woods around haunted castle
        elif (roomnumber == 1):
            self.talker = None
            self.room = Maproom1(self.x,self.y)
        elif (roomnumber == 1.1):
            self.talker = None
            self.room = Maproom1_1(self.x,self.y)
        elif (roomnumber == 1.2):
            self.talker = None
            self.room = Maproom1_2(self.x,self.y)
        elif (roomnumber == 1.3):
            self.talker = None
            self.room = Maproominn1_3(self.x,self.y)
        elif (roomnumber == 1.4):
            self.talker = None
            self.room = Maproominn1_4(self.x,self.y)
        elif (roomnumber == 1.5):
            self.talker = None
            self.room = Maproominn1_5(self.x,self.y)
        elif (roomnumber == 1.6):
            self.talker = None
            self.room = Maproominn1_6(self.x,self.y)
        # NOTE left woods of haunted castle
        elif (roomnumber == "1.1.1"):
            self.talker = None
            self.room = Maproom1_1_1(self.x,self.y)
        # rooms of haunted castle    
        elif (roomnumber == 2):
            self.talker = None
            self.room = Maproom2(self.x,self.y)
        elif (roomnumber == 3):
            self.talker = None
            self.room = Maproom3(self.x,self.y)
        elif (roomnumber == 4):
            self.talker = None
            self.room = Maproom4(self.x,self.y)
        elif (roomnumber == 5):
            self.talker = None
            self.room = Maproom5(self.x,self.y)
        elif (roomnumber == 6):
            self.talker = None
            self.room = Maproom6(self.x,self.y)
        elif (roomnumber == 7):
            self.talker = None
            self.room = Maproom7(self.x,self.y)
        elif (roomnumber == 8):
            self.talker = None
            self.room = Maproom8(self.x,self.y)
        elif (roomnumber == 9):
            self.talker = None
            self.room = Maproom9(self.x,self.y)
        elif (roomnumber == 10):
            self.talker = None
            self.room = Maproom10(self.x,self.y)
        elif (roomnumber == 11):
            self.talker = None
            self.room = Maproom11(self.x,self.y)
        elif (roomnumber == 12):
            self.talker = None
            self.room = Maproom12(self.x,self.y)
        elif (roomnumber == 13):
            self.talker = None
            self.room = Maproom13(self.x,self.y)
        elif (roomnumber == 14):
            self.talker = None
            self.room = Maproom14(self.x,self.y)
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
	    print "collision with ClickRect!"
            return 1 
        else:
            return 0 

            
if __name__ == "__main__":
    foo = JohnTheSorcererMain()



