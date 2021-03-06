#!/usr/bin/env python3

import sys

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []

    # For each test case
    for _ in range(T):
        # Read the input data
        n = int(io.readline())
        a = list(map(int, io.readline().strip().split()))
        # Add to the list fo test cases
        tc.append((n,a))

    # Return all the test cases parsed
    return tc

# Function to solve a single test case
def solve_testcase(t):
    # Get data from the test case
    (n,a) = t

    cnt = 0
    for i in range(0,n):
        if a[i] > 0:
            cnt+= a[i]
    return cnt

# Solve 
def solve(input, output):
    # Enumerate all the test cases
    for i, t in enumerate(parse_testcases(input)):
        # Print the solution of the test case
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

if __name__ == "__main__":
    #fin = sys.stdin
    #fout = sys.stdout
    # If you want to read and write from files use these two lines:
    fin = open(r'C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\input.txt', "r")
    fout = open(r"C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\output.txt", "w")
    solve(fin, fout)