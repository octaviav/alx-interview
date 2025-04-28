#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): Each list represents a box
        and contains keys to other boxes

    Returns:
        bool: True if all boxes can be opened, else False
    """
    # Number of boxes
    x = len(boxes)

    unlocked = [False] * x
    unlocked[0] = True  # First box is already unlocked

    keys_to_check = boxes[0][:]

    while keys_to_check:
        key = keys_to_check.pop()

        if key < x and not unlocked[key]:
            unlocked[key] = True

            keys_to_check.extend(boxes[key])

    return all(unlocked)
