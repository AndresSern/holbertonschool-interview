#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
        Function that dermines if all the boxes can be opened
    """
    keys = set(boxes[0])
    count = 0
    for rows in boxes:
        if rows == []:
            count += 1
        else:
            keys = (keys | set(rows))
    if count == 0:
        return len(boxes) == len(boxes)
    return (len(keys)  == (len(boxes) - count))
