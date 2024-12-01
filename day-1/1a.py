import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

list_one = []
list_two = []

for line in f:
    list_one.append(int(line.split()[0]))
    list_two.append(int(line.split()[1]))

list_one.sort()
list_two.sort()

total_distance = 0

for i, j in zip(list_one, list_two):
    total_distance += abs(i - j)

print(f"The total distance is:%i", total_distance)
