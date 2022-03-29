#!/usr/bin/env python
# coding: utf-8

from numpy import median

opening = {"(": ")", "{": "}", "[": "]", "<":">"}
closing = {v:k for k,v in opening.items()}
scores_first = {')': 3, '}': 1197, ']': 57, '>': 25137}
scores_second = {')': 1, '}': 3, ']': 2, '>': 4}


def calculate_scores(lines, get_incomplete=False):
    score_corrupted = 0
    scores_incomplete = []
    for line in lines:
        stack = []
        for char in line:
            if char in opening.keys():
                stack.append(char)
            else:
                if stack[-1] == closing[char]:
                    stack.pop()
                else:
                    score_corrupted += scores_first[char]
                    stack = []
                    break
        if stack:
            score = 0
            for bracket in reversed(stack):
                score = score*5 + scores_second[opening[bracket]]
            scores_incomplete.append(score)
    if not get_incomplete:
        return score_corrupted
    else:
        return int(median(scores_incomplete))

def read_input(input_file):
    with open(input_file, "r") as file:
        return [line.strip() for line in file]

def solve_first(input):
    return calculate_scores(input)

def solve_second(input):
    return calculate_scores(input, get_incomplete=True)

if __name__ == "__main__":
    my_input = read_input("../../input/input_10.txt")
    print(solve_first(my_input))
    print(solve_second(my_input))