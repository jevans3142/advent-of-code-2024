import os
import re

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

total = 0

for line in f:
    list = re.findall(r"mul\((\d+),(\d+)\)", line)
    for item in list: 
        total += int(item[0]) * int(item [1])

print(total)