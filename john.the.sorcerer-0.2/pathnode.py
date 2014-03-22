
# Copyright (C) Benjamin Woodruff 2011 
# Copyright (C) Johan Ceuppens 2014 
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

import math

class Node(object):
    def __init__(self, x, y):
        super(Node, self).__init__()
        self.x, self.y = float(x), float(y)
        self.visible_siblings = set()
    
    def dist(self, point):
        return math.hypot(self.x - point.x, self.y - point.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __repr__(self):
        return "Node" + self.__str__()
    
    def __hash__(self):
        return hash(self.x)^hash(self.y)
