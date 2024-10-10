#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if type(boxes) is not list or len(boxes) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = k in boxes[i] and k != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
