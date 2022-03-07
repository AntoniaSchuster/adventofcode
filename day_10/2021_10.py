#!/usr/bin/env python
# coding: utf-8

from numpy import median

opening = {"(": ")", "{": "}", "[": "]", "<":">"}
closing = {v:k for k,v in opening.items()}
scores_first = {')': 3, '}': 1197, ']': 57, '>': 25137}
scores_second = {')': 1, '}': 3, ']': 2, '>': 4}


def calculate_scores(lines):
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
    print(f"The answer for task 1 is: {score_corrupted}")
    print(f"The answer for task 2 is: {int(median(scores_incomplete))}")


with open("test.txt", "r") as file:
    test = [line.strip() for line in file]
calculate_scores(test)

with open("input.txt", "r") as file:
    myinput = [line.strip() for line in file]
calculate_scores(myinput)

