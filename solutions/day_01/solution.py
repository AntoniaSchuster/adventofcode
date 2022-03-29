#!/usr/bin/env python
# coding: utf-8

def read_input(input_file):
    with open(input_file, "r") as file:
        return [int(line.strip()) for line in file]

def solve_first(input):
    return sum([l1<l2 for l1,l2 in zip(input, input[1:])])

def solve_second(input, window_size=3):
    sums = [sum(input[n:n+window_size]) for n, _ in enumerate(input) if n <= len(input)-window_size]
    return solve_first(sums)
#     alternative: return sum([sum([l1,l2,l3])<sum([l2,l3,l4]) for l1,l2,l3,l4 in zip(input, input[1:], input[2:], input[3:])])
	

if __name__ == "__main__":
    my_input = read_input("../../input/input_01.txt")
    print(solve_first(my_input))
    print(solve_second(my_input))
