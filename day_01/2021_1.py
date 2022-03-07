#!/usr/bin/env python
# coding: utf-8

def solve_first(input):
    return sum([l1<l2 for l1,l2 in zip(input, input[1:])])
def solve_second(input, window_size):
    sums = [sum(input[n:n+window_size]) for n, _ in enumerate(input) if n <= len(input)-window_size]
    return solve_first(sums)
#     alternative: return sum([sum([l1,l2,l3])<sum([l2,l3,l4]) for l1,l2,l3,l4 in zip(input, input[1:], input[2:], input[3:])])
	
with open("test.txt", "r") as file:
    test = [int(line.strip()) for line in file]
print("Test:")
print(solve_first(test))
print(solve_second(test,3))

with open("input.txt", "r") as file:
    input = [int(line.strip()) for line in file]
print("My input:")
print(solve_first(input))
print(solve_second(input, 3))

