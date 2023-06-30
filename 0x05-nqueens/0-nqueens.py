#!/usr/bin/python3
"""place N non-attacking queens on an N×N chessboard"""
import sys


solutions = []
n = 0
pos = None


def get_input():
    """Parse user input"""
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    """Checks if positions of two queens is attacking"""
    if (pos1[0] == pos2[0]) or (pos1[1] == pos2[1]):
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions."""
    global solutions
    for solution in solutions:
        i = 0
        for sin_pos in solution:
            for grp_pos in group:
                if sin_pos[0] == grp_pos[0] and sin_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Builds a solution"""
    global solutions
    global n
    if row == n:
        temp = group.copy()
        if not group_exists(temp):
            solutions.append(temp)
    else:
        for col in range(n):
            index = (row * n) + col
            matches = zip(list([pos[index]]) * len(group), group)
            occupied = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[index].copy())
            if not any(occupied):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for a chessboard of size n"""
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    index = 0
    group = []
    build_solution(index, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
