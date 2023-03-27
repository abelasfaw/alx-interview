#!/usr/bin/python3
'''Module that checks if all boxes can be opened'''


def canUnlockAll(boxes):
    current = boxes[0]
    tobeopened = []
    for i in range(1, len(boxes)):
        tobeopened.append(i)
    accessible = []
    while (True):
        for key in current:
            if key in tobeopened:
                del tobeopened[tobeopened.index(key)]
                accessible.append(key)
                if (len(tobeopened) == 0):
                    return True
        if (len(accessible) == 0 and len(tobeopened) != 0):
            return False
        current = boxes[accessible[0]]
        del accessible[0]
