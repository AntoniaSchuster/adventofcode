#!/usr/bin/env python
# coding: utf-8

class command:
    def __init__(self, command_string):
        split = command_string.split()
        self.direction = split[0]
        self.amount = int(split[1])

class position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        
    def __repr__(self):
        return f"Horizontal position: {self.horizontal}\nDepth: {self.depth}\nResult: {self.horizontal*self.depth}"
    
    def execute(self, command):
        if command.direction == "up":
            self.depth -= command.amount
        elif command.direction == "down":
            self.depth += command.amount
        elif command.direction == "forward":
            self.horizontal += command.amount
            
    def execute_corrected(self, command):
        if command.direction == "up":
            self.aim -= command.amount
        elif command.direction == "down":
            self.aim += command.amount
        elif command.direction == "forward":
            self.horizontal += command.amount
            self.depth += self.aim * command.amount
        
def parse_input(input):
    return [command(line) for line in input]

def run_first(input):
    commands = parse_input(input)
    p = position()
    for c in commands:
        p.execute(c)
    print(p)
    
def run_second(input):
    commands = parse_input(input)
    p = position()
    for c in commands:
        p.execute_corrected(c)
    print(p)

with open("test.txt", "r") as file:
    test = [line.strip() for line in file]
print("Test:")
run_first(test)
run_second(test)

with open("input.txt", "r") as file:
    input = [line.strip() for line in file]
print("\nMy input:")
run_first(input)
run_second(input)