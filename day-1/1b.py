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

total_similarity = 0

for i in list_one:
    total_similarity += i * list_two.count(i)

print(f"The total similarity is:%i", total_similarity)
