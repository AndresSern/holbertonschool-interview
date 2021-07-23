#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
        Function that dermines if all the boxes can be opened
    """
    allKeys = [0]
    lenBoxes = len(boxes)
    for rows in allKeys:
        for key in boxes[rows]:
            if key > lenBoxes:
                return False
            if key not in allKeys:
                allKeys.append(key)

    return (len(allKeys )  == (lenBoxes))
