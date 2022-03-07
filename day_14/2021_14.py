#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict

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
        print(max(counts.values())-min(counts.values()))
        
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
        print(max(count_chars.values())-min(count_chars.values()))
        
with open("test.txt", "r") as file:
    test_template = file.readline().strip()
    file.readline()
    test_rules = [line.strip() for line in file.readlines()]
    
print("Test:")

poly = Poly(test_template, test_rules)
for n in range(10):
    poly.polymerize()
poly.calculate_result()

poly = Poly(test_template, test_rules)
poly.calculate_result_fast(40)


with open("input.txt", "r") as file:
    my_template = file.readline().strip()
    file.readline()
    my_rules = [line.strip() for line in file.readlines()]

print("My input:")

poly = Poly(my_template, my_rules)
for n in range(10):
    poly.polymerize()
poly.calculate_result()

poly = Poly(my_template, my_rules)
poly.calculate_result_fast(40)

