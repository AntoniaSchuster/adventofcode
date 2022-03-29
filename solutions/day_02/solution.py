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


def read_input(input_file):
    with open(input_file, "r") as file:
        return [line.strip() for line in file]

def solve_first(input):
    commands = [command(line) for line in input]
    p = position()
    for c in commands:
        p.execute(c)
    return p.horizontal*p.depth

def solve_second(input):
    commands = [command(line) for line in input]
    p = position()
    for c in commands:
        p.execute_corrected(c)
    return p.horizontal*p.depth

if __name__ == "__main__":
    my_input = read_input("../../input/input_02.txt")
    print(solve_first(my_input))
    print(solve_second(my_input))