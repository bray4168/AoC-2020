array = []

with open('Day_1/input.txt', 'r') as file:
  for line in file:
    array.append(int(line))

for num_1 in array:
  for num_2 in array:
    for num_3 in array:
      if num_1 + num_2 + num_3 == 2020:
        print(num_1 * num_2 * num_3)

