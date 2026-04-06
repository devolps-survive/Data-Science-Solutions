# Python Foundations -- Daily Assignment Solutions

This repository contains three fundamental Python programs built using functions and efficient logic:

1. Prime Number Checker (Optimized O(√n) solution)
2. Largest Number Finder in a List
3. CLI-based Calculator

## 📌 1. Prime Number Checker (Efficient O(√n) Approach)

### Description
Checks whether a number is prime using an optimized algorithm that reduces unnecessary iterations.

### Key Optimization
Instead of checking all numbers from `2 to n-1`, we only check up to:


### Why this works
If `n = a × b`, at least one factor must be ≤ √n.

### Logic Flow
- If number ≤ 1 → Not prime
- Check divisibility from 2 to √n
- If any divisor found → Not prime
- Else → Prime

### Example
    Input: 17
    Output: Prime

## 📌 2. Largest Number in a List

### Description
Finds the maximum value in a list using Python manual approaches.
### Example
    Input: [2, 4, 6, 10, 3]
    Output: 10

## 📌 3. CLI-Based Calculator (Using Functions)

### Description
A command-line calculator that performs basic arithmetic operations using modular functions.

### Features
- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling)
- Function-based structure

### Core Idea
Each operation is implemented as a separate function, and user input determines which function is executed.

### Example
    Enter first number: 10
    Enter operator: *
    Enter second number: 5
    Result: 50
