from functools import reduce

file_array = []

with open('Day_3/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)


# puzzle 1
slope_right = 3
slope_down = 1
down_index = 0
right_index = 0
trees_1 = 0

while down_index != (len(file_array) - 1):
  down_index = down_index + slope_down
  right_index = (right_index + slope_right) % (len(file_array[down_index]) - 1)
  if file_array[down_index][right_index] == "#":
    trees_1 += 1
    print(down_index, right_index)

# puzzle 2
slope_right = [1, 3, 5, 7, 1]
slope_down = [1, 1, 1, 1, 2]
answer_array = []
answer = 0

for index in range(len(slope_right)):
  trees = 0
  down_index = 0
  right_index = 0
  while down_index < (len(file_array) - 1):
    down_index = down_index + slope_down[index]
    right_index = (right_index + slope_right[index]) % (len(file_array[down_index]) - 1)
    if file_array[down_index][right_index] == "#":
      trees += 1
  answer_array.append(trees)

answer = reduce((lambda x, y: x * y), answer_array)

print("Puzzle 1 solution: " + str(trees_1))
print("Puzzle 2 solution: " + str(answer))