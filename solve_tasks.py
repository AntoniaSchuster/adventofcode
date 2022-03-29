#!/usr/bin/env python
# coding: utf-8

import importlib 
import sys

DAY = "{:02}".format(int(sys.argv[1]))

def solve(input, part):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        print(f"The answer to part {part} is:", end="")
        print(f"{solve(input):>10}")


solution    = importlib.import_module(f"solutions.day_{DAY}.solution")
reader      = getattr(solution, "read_input")
my_input    = reader(f"input/input_{DAY}.txt")


print(f"Day {DAY.lstrip('0')}")

solve(my_input, 1)
solve(my_input, 2)




