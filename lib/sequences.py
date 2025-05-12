#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []

    for i in range(length):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            next_num = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_num)

    print(fibonacci)
print_fibonacci(12)