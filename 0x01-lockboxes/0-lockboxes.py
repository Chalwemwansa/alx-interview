#!/usr/bin/python3
"""module contains a function that checks if the boxes
    list of lists can unlock all other boxes"""


def canUnlockAll(boxes):
    """the function that checks if boxes can be opened
      make a list and add all the unique keys we have in the different
      boxes and then check the range"""
    lst = []
    for key in boxes[0]:
        if key in range(1, len(boxes)):
            lst.append(key)
    for key in lst:
        if key in range(1, len(boxes)):
            for i in boxes[key]:
                if i in range(1, len(boxes)) and i not in lst:
                    index = lst.index(key) + 1
                    lst.insert(index, i)
    if __name__ == '__main__':
        print(lst)
    if len(lst) >= len(boxes) - 1:
        return True
    return False


if __name__ == '__main__':
    """True True False expected for the three different examples below"""
    print(canUnlockAll([[1], [2], [3], [4], []]))
    print(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1],
                       [6]]))
    print(canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))
