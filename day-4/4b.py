import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

lines = []

for line in f:
    lines.append(line.rstrip())

line_length = len(lines[0])

number_of_xmases = 0

def access_char(row, col):
    if not 0 <= col < line_length:
        return "."
    if not 0 <= row < len(lines):
        return "."
    return lines[row][col]


def test_a_direction(start_row,start_col,M1,M2,S1,S2):
    if not access_char(start_row+M1[0],start_col+M1[1]) == "M":
        return False
    if not access_char(start_row+M2[0],start_col+M2[1]) == "M":
        return False
    if not access_char(start_row+S1[0],start_col+S1[1]) == "S":
        return False
    if not access_char(start_row+S2[0],start_col+S2[1]) == "S":
        return False
    return True 


for row in range(len(lines)):
    for column in range(line_length):
        if lines[row][column] == "A":
            # Ms on left
            if test_a_direction(row,column,[-1,-1],[1,-1],[1,1],[-1,1]): number_of_xmases += 1
            # Ms on right
            if test_a_direction(row,column,[-1,1],[1,1],[1,-1],[-1,-1]): number_of_xmases += 1
            # Ms on top
            if test_a_direction(row,column,[-1,-1],[-1,1],[1,1],[1,-1]): number_of_xmases += 1
            # Ms on bottom
            if test_a_direction(row,column,[1,-1],[1,1],[-1,1],[-1,-1]): number_of_xmases += 1


print(number_of_xmases)
