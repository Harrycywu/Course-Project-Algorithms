# Class: CS 325
# Student: Cheng Ying Wu
# Assignment: HW6-Q5
# Description: Apply BFS/DFS/MST to solve a problem (Portfolio Project Problem).

# Import deque
from collections import deque


def solve_puzzle(Board, Source, Destination):
    """
    Given a 2-D puzzle of size MxN that has N rows and M columns. Each cell in the puzzle is either empty or has
    a barrier. An empty cell is marked by "-" (hyphen), and the one with a barrier is marked by "#".

    Given two coordinates from the puzzle (a,b)-Source and (x,y)-Destination, return the minimum number of cells that
    you have to cover to reach the destination cell.

    ** Extra Credit: Return a set of possible directions as well in the form of a string.
    """
    # Checks whether the source and destination coordinates have barriers
    if Board[Source[0]-1][Source[1]-1] == "#" or Board[Destination[0]-1][Destination[1]-1] == "#":
        # If yes, returns None
        return None

    # Gets the number of rows and columns
    num_row = len(Board)
    num_col = len(Board[0])

    # Implement the BFS algorithm
    # Initializes the number of cells to be returned as None
    ret_num = None

    # Tracks each level moves
    level_move = dict()

    # Initializes an empty list of visited coordinates
    visited_lst = []

    # Initializes an empty queue (implemented by a deque) and adds the starting coordinate to the queue
    queue = deque([str(Source[0]) + str(Source[1])])

    # If the queue is not empty, dequeue a coordinate
    while queue:
        # queue: First in First out
        deq_coord = queue.popleft()

        # Checks the current distance to the source
        if ret_num is None:
            distance = abs(int(deq_coord[0]) - Source[0]) + abs(int(deq_coord[1]) - Source[1])
            if distance > 1:
                ret_num = 1

        # Updates the number of cells to be returned
        if ret_num is not None:
            distance = abs(int(deq_coord[0]) - Source[0]) + abs(int(deq_coord[1]) - Source[1]) - ret_num
            if distance > 1:
                ret_num += 1

        # Tracks each level moves
        if ret_num not in level_move:
            level_move[ret_num] = [deq_coord]
        else:
            if deq_coord not in level_move[ret_num]:
                level_move[ret_num].append(deq_coord)

        # Checks whether it is the ending coordinate
        if deq_coord == (str(Destination[0]) + str(Destination[1])):
            # If it is the ending coordinate, then stop!
            visited_lst.append(deq_coord)

            # Returns the result: ret_num
            # if ret_num is None:
            #     ret_num = 0
            # return ret_num

            # Calls the extra credit helper method
            if ret_num is None:
                ret_num = 0
            return extra_credit(ret_num, level_move, visited_lst[0], visited_lst[-1])

        # Adds it to the list of visited coordinates
        if deq_coord not in visited_lst:
            visited_lst.append(deq_coord)

        # Gets the possible next move of the current coordinate
        poss_move = [str(int(deq_coord[0])+1)+deq_coord[1], str(int(deq_coord[0])-1)+deq_coord[1],
                     deq_coord[0]+str(int(deq_coord[1])+1), deq_coord[0]+str(int(deq_coord[1])-1)]

        # Checks whether these possible moves are valid
        for move in poss_move:
            if int(move[0]) > num_row or int(move[1]) > num_col or int(move[0]) < 1 or int(move[1]) < 1:
                # If it is out of the Board, continue
                continue
            elif Board[int(move[0])-1][int(move[1])-1] == "#":
                # If there is a barrier, continue
                continue

            # If the possible next move is not in the list of visited coordinates, enqueues it into the queue
            if move not in visited_lst:
                queue.append(move)

    # Cannot not reach the destination
    return None


def extra_credit(num_cell, level_move, start, end):
    """
    Takes the number of cells, the dictionary to record the move, the starting coordinates, and the ending coordinates
    as inputs, and returns a tuple (number of cells, a set of possible directions in the form of a string).
    """
    # Checks Special case
    poss_direction = ""
    if num_cell == 0:
        if (int(start[0]) - int(end[0])) < 0:
            poss_direction += "D"
        elif (int(start[0]) - int(end[0])) > 0:
            poss_direction += "U"
        elif (int(start[1]) - int(end[1])) < 0:
            poss_direction += "R"
        elif (int(start[1]) - int(end[1])) > 0:
            poss_direction += "L"

        ret_str = poss_direction[::-1]
        return len(poss_direction) - 1, ret_str

    # Initial Settings
    num_cell -= 1
    current = end

    # Loops through the moves at each level and gets a set of possible directions in the form of a string
    while num_cell > 0:
        for move in level_move[num_cell]:
            if (abs(int(current[0]) - int(move[0])) + abs(int(current[1]) - int(move[1]))) != 1:
                continue
            else:
                if (int(move[0]) - int(current[0])) < 0:
                    poss_direction += "D"
                elif (int(move[0]) - int(current[0])) > 0:
                    poss_direction += "U"
                elif (int(move[1]) - int(current[1])) < 0:
                    poss_direction += "R"
                elif (int(move[1]) - int(current[1])) > 0:
                    poss_direction += "L"
                current = move
                num_cell -= 1

    for move in level_move[None]:
        if (abs(int(current[0]) - int(move[0])) + abs(int(current[1]) - int(move[1]))) != 1:
            continue
        else:
            if (int(move[0]) - int(current[0])) < 0:
                poss_direction += "D"
            elif (int(move[0]) - int(current[0])) > 0:
                poss_direction += "U"
            elif (int(move[1]) - int(current[1])) < 0:
                poss_direction += "R"
            elif (int(move[1]) - int(current[1])) > 0:
                poss_direction += "L"
            current = move

    if (int(start[0]) - int(current[0])) < 0:
        poss_direction += "D"
    elif (int(start[0]) - int(current[0])) > 0:
        poss_direction += "U"
    elif (int(start[1]) - int(current[1])) < 0:
        poss_direction += "R"
    elif (int(start[1]) - int(current[1])) > 0:
        poss_direction += "L"

    # Since I choose to get the direction from backward, so reverse the current string
    ret_str = poss_direction[::-1]

    # Returns the result
    return len(poss_direction) - 1, ret_str


# Test Cases
if __name__ == '__main__':
    print("\nExample 1")
    board = [["-", "-", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "-", "-", "-", "-"],
             ["#", "-", "#", "#", "-"],
             ["-", "#", "-", "-", "-"]]

    print("\nQ1")
    source = (1, 3)
    target = (3, 3)
    print(solve_puzzle(board, source, target))   # 3, LDDR

    print("\nQ2")
    source = (1, 1)
    target = (5, 5)
    print(solve_puzzle(board, source, target))   # 7, DDRRRRDD

    print("\nQ3")
    source = (1, 1)
    target = (5, 2)
    print(solve_puzzle(board, source, target))   # None

    print("\nExample 2")
    board = [["-", "#", "-", "-"],
             ["-", "-", "#", "-"],
             ["#", "-", "-", "-"],
             ["-", "-", "#", "#"],
             ["#", "-", "-", "-"]]

    print("\nQ1")
    source = (1, 1)
    target = (3, 3)
    print(solve_puzzle(board, source, target))  # 3

    print("\nQ2")
    source = (2, 4)
    target = (5, 2)
    print(solve_puzzle(board, source, target))  # 4

    print("\nQ3")
    source = (1, 1)
    target = (2, 1)
    print(solve_puzzle(board, source, target))  # 0
