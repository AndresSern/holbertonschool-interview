#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
        Function that dermines if all the boxes can be opened
    """
    lenBoxes = len(boxes)

    if not isinstance(boxes, list) or lenBoxes == 0:
        return False
    allKeys = [0]

    for rows in allKeys:
        tempBox = boxes[rows]
        if not isinstance(tempBox, list):
            return False
        for key in tempBox:
            if key >= lenBoxes:
                continue
            if key not in allKeys:
                allKeys.append(key)

    return (len(allKeys) == (lenBoxes))
