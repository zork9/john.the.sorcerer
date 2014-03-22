
# Copyright (C) Johan Ceuppens 2010-2013 
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
from taskbarbutton import *
from roompath import *

import pathgeometry
import pathmapping
from pathnode import Node

class Room1Path(RoomPath):
    "Create room 1 polygons for pathfinding"
    def __init__(self, start = Node(550, 430)):
	self.side1 = pathgeometry.Polygon((0, 0), (640, 0), (640, 100), (0, 100),
      	                         ccw=False)
	self.side2 = pathgeometry.Polygon((0, 400), (640, 400), (640, 480), (0, 480),
       	                         ccw=False)

	self.room_board.add(self.side1)
	self.room_board.add(self.side2)

	self.player_start = start 

###    find_path(self, endx, endy):
###    set_player_position(self, endx, endy):

