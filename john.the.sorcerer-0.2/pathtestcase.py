
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

import pathgeometry
import pathmapping
from pathnode import Node
import unittest

# build the board in the example at
# https://github.com/CBCJVM/CBCJVM/wiki/pathfinding_proposal
# This is kind of an s-curve
# (0, 0) ______________     ________ (5, 0)
#       |        (3, 0)| E |(4, 0)  |
#       |              |   |        |
#       | (1, 1) ______|   |        |
#       |       |   (3, 1) |        |
#       |       |    ______|(4, 2)  |
#       |       |   |(2, 2)         |
#       |       |   |               |
#       |_(1,_3)| S |(2,_3)___(5,_3)|
# (0, 3)
s_left_side = pathgeometry.Polygon((0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3),
                               ccw=False)
s_right_side = pathgeometry.Polygon((4, 0), (5, 0), (5, 3), (2, 3), (2, 2), (4, 2),
                                ccw=False)
s_board = pathmapping.Board()
s_board.add(s_left_side); s_board.add(s_right_side)
s_start = Node(1.5, 3)
s_end = Node(3.5, 0)
# del left_side; del right_side

# A simple rectangular board, to test that a path cannot pass through a polygon
# (0, 0) ________ (1, 0)
#       |        |
#       |        |
#       |________|
# (0, 1)          (1, 1)
r_board = pathmapping.Board()
r_board.add(pathgeometry.Polygon((0, 0), (1, 0), (1, 1), (0, 1), ccw=False))
r_start = Node(0, 0)
r_end = Node(1, 1)

class TestContainsNodeInArea(unittest.TestCase):
    def test_s_curve_node_in_area(self):
        assert s_left_side.contains_node_in_area(Node(2, .5))
        assert s_left_side.contains_node_in_area(Node(1, 2.5))
        assert not s_left_side.contains_node_in_area(Node(3.5, .5))
        assert not s_right_side.contains_node_in_area(Node(3.5, .5))

class TestTriangulation(unittest.TestCase):
    def test_s_curve_triangulation(self):
        print(s_left_side.triangles)
        print(s_right_side.triangles)

class TestExpansion(unittest.TestCase):
    def test_r_expansion(self):
        print("Expanded r: " + str(r_board.get_expanded(.25)))
    
    def test_s_expansion(self):
        print("Expanded s: " + str(s_board.get_expanded(.25)))

class TestLineOfSight(unittest.TestCase):
    def test_s_curve_is_visible(self):
        # returns false every time!!!
        
        assert not s_board.is_visible(s_start, s_end)
        assert s_board.is_visible(Node(1.5, 2), Node(1.5, 2.5))
        assert s_board.is_visible(Node(1.4, 2), Node(1.6, 2.5))
        assert not s_board.is_visible(Node(3, 1), Node(5, 3))
        assert s_board.is_visible(Node(3, 0), Node(3, 1))
        assert s_board.is_visible(Node(2, 3), Node(1, 1))
    
    def test_s_curve_visible_set(self):
        assert s_board.get_visible_set(Node(1.5, 2.5)) == \
               set([Node(2.0, 2.0), Node(2.0, 3.0), Node(1.0, 3.0),
                    Node(1.0, 1.0)])
        
        # There are two valid answers here
        s = s_board.get_visible_set(Node(2, 3))
        a = set([Node(5, 3), Node(1, 3), Node(2, 2), Node(1, 1)])
        b = set([Node(5, 3), Node(1, 3), Node(2, 2), Node(1, 1), Node(0, 3)])
        assert s == a or s == b
    
    def test_r_board(self):
        assert not r_board.is_visible(r_start, r_end)

class TestPathfinding(unittest.TestCase):
    def test_s_curve_path(self):
        s_path = [Node(2.0, 2.0), Node(3.0, 1.0), s_end]
        assert s_board.get_shortest_path(s_start, s_end) == s_path
        # try it backwards too
        s_back_path = [Node(3.0, 1.0), Node(2.0, 2.0), s_start]
        assert s_board.get_shortest_path(s_end, s_start) == s_back_path

if __name__ == "__main__":
    unittest.main()
else:
    raise Exception("testcase.py is meant only to be run directly.")
