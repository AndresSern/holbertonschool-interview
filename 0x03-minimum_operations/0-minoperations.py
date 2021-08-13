#!/usr/bin/python3
"""
    Min Operations Copy and paste
"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given a
    number n, write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0
    num = n
    div = 2
    Operati = 0

    while num > 1:
        if num % div == 0:
            num /= div
            Operati += + div
        else:
            div += 1
    return Operati
