#!/usr/bin/env python
# coding: utf-8

import numpy as np
from collections import defaultdict
from itertools import cycle

class Position:
    def __init__(self, pos_str):
        self.x, self.y = [int(xy) for xy in pos_str.split(',')]
    def __repr__(self):
        return str((self.x,self.y))

class Line:
    def __init__(self, start_end):
        self.start, self.end = [Position(p) for p in start_end.split(" -> ")]
        points_x = np.linspace(self.start.x,self.end.x, abs(self.end.x-self.start.x)+1, dtype=int)
        points_y = np.linspace(self.start.y,self.end.y, abs(self.end.y-self.start.y)+1, dtype=int)
        self.diagonal = False
        if len(points_x) > len(points_y):
            self.points = [Position(f"{px},{py}") for px, py in zip(points_x, cycle(points_y))]
        elif len(points_x) < len(points_y):
            self.points = [Position(f"{px},{py}") for px, py in zip(cycle(points_x), points_y)]
        else:
            self.points = [Position(f"{px},{py}") for px, py in zip(points_x, points_y)]
            self.diagonal = True

class Field:
    def __init__(self):
        self.vents = defaultdict(int)
        
    def __repr__(self):
        return str(self.vents)
        
    def update_vents(self, line, diagonal=False):
        if not line.diagonal:
            for p in line.points:
                self.vents[str(p)] +=1
        if diagonal:
            if line.diagonal:
                for p in line.points:
                    self.vents[str(p)] +=1
    
    def count_overlaps(self):
        overlaps = sum([1 for n in self.vents.values() if n > 1])
        print(f"Number of overlaps: {overlaps}")

def run(myinput, diagonal=False):
	field = Field()
	lines = [Line(l) for l in myinput]
	for l in lines:
		field.update_vents(l, diagonal)
	field.count_overlaps()
	
with open("test.txt", "r") as file:
    test = [line.strip() for line in file]

print("Test:")
run(test)
run(test, diagonal=True)

with open("input.txt", "r") as file:
    my_input = [line.strip() for line in file]
	
print("My input:")
run(my_input)
run(my_input, diagonal=True)





