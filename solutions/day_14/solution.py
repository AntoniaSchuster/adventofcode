#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
from re import template

class Poly:
    
    def __init__(self, template, rules):
        self.current = list(template)
        self.rules = {k:v for k,v in [r.split(' -> ') for r in rules]}
        self.counter = defaultdict(int)
        
    def polymerize(self):
        new_current = self.current[0]
        for n in range(len(self.current)-1):
            pair = "".join(self.current[n:n+2])
            new_current += self.rules[pair]
            new_current += pair[1]
        self.current = new_current
        
    def calculate_result(self):
        counts = defaultdict(int)
        for e in self.current:
            counts[e] += 1
        return max(counts.values())-min(counts.values())
        
    def calculate_result_fast(self, iterations):
        pairs = ["".join(pair) for pair in zip(self.current, self.current[1:])]
        for pair in pairs:
            self.counter[pair] += 1
        last_letter = self.current[-1]
        
        for n in range(iterations):
            tmp = defaultdict(int)
            for p, c in self.counter.items():
                if c > 0:
                    tmp[p] -= c
                    tmp[p[0] + self.rules[p]] += c
                    tmp[self.rules[p] + p[1]] += c
            for p, c in tmp.items():
                self.counter[p] += c
        count_chars = defaultdict(int)
        
        for p, c in self.counter.items():
            count_chars[p[0]] += c
        count_chars[last_letter] += 1
        return max(count_chars.values())-min(count_chars.values())

def read_input(input_file):
    with open(input_file, "r") as file:
        template = file.readline().strip()
        file.readline()
        rules = [line.strip() for line in file.readlines()]
        return template, rules

def solve_first(input):
    template, rules = input
    poly = Poly(template, rules)
    for n in range(10):
        poly.polymerize()
    return poly.calculate_result()

def solve_second(input):
    template, rules = input
    poly = Poly(template, rules)
    return poly.calculate_result_fast(40)

if __name__ == "__main__":
    my_input = read_input("../../input/input_14.txt")
    print(solve_first(my_input))
    print(solve_second(my_input))





