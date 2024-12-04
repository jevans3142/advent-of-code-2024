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

def test_a_direction(start_row, start_col, row_interval, col_interval):
    output_str = (access_char(start_row, start_col) + 
                  access_char(start_row + row_interval, start_col + col_interval) + 
                  access_char(start_row + row_interval * 2, start_col + col_interval * 2) + 
                  access_char(start_row + row_interval * 3, start_col + col_interval * 3) ) 
    return True if output_str == "XMAS" else False 

for row in range(len(lines)):
    for column in range(line_length):
        if lines[row][column] == "X":
            # Forwards
            if test_a_direction(row,column,0,1): number_of_xmases += 1
            # Backwards
            if test_a_direction(row,column,0,-1): number_of_xmases += 1
            # Upwards
            if test_a_direction(row,column,-1,0): number_of_xmases += 1
            # Downwards
            if test_a_direction(row,column,1,0): number_of_xmases += 1
            # Fowards and up
            if test_a_direction(row,column,-1,1): number_of_xmases += 1
            # Backwards and up
            if test_a_direction(row,column,-1,-1): number_of_xmases += 1
            # Fowards and down
            if test_a_direction(row,column,1,1): number_of_xmases += 1
            # Backwards and down
            if test_a_direction(row,column,1,-1): number_of_xmases += 1

print(number_of_xmases)