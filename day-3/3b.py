import os
import re

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

total = 0

complete_string = '"'

for line in f:
    complete_string += line

sections = re.split(r"(don't\(\))|(do\(\))", complete_string)
results = list(filter(None, sections))

mults_enabled = True
total = 0

for section in results:
    print(section)
    if section == "do()":
        mults_enabled = True
        continue
    if section == "don't()":
        mults_enabled = False
        continue
    if mults_enabled == False:
        continue
    list = re.findall(r"mul\((\d+),(\d+)\)", section)
    for item in list:
        total += int(item[0]) * int(item[1])

print(total)

#     list = re.findall(r"mul\((\d+),(\d+)\)", line)
#     for item in list:
#         total += int(item[0]) * int(item[1])

# # list_excluded = re.findall(r"don't\(\).*?(?:.*?mul\((\d+),(\d+)\).*?)*.*?do\(\)", complete_string)
# list_excluded = re.findall(r"don't\(\)(.*?)do\(\)", complete_string)

# for section in list_excluded:
#     print(section)
#     list = re.findall(r"mul\((\d+),(\d+)\)", section)
#     for item in list:
#         total -= int(item[0]) * int(item[1])
