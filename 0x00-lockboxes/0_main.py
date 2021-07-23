#!/usr/bin/env python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

""" FALSE """
boxes = [[1], 2]
print(canUnlockAll(boxes))

""" False """
boxes = ["Doing A Test", [1]]
print(canUnlockAll(boxes))

""" False """
boxes = {"A":3}
print(canUnlockAll(boxes))
