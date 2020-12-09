file_array = []

# Read file into lines
with open('Day_9/input.txt', 'r') as file:
  for line in file:
    file_array.append(line.strip())

preamble_range = 25
invalid_number = 0

def form_sum_array(index):
  sum_array = []
  for each in range(index - preamble_range, index):
    for number in range(index - preamble_range, index):
      if each == number:
        continue
      else:
        sum_array.append(int(file_array[each]) + int(file_array[number]))
  return sum_array

def find_number_set(index):
  sum = 0
  max = 0
  min = int(file_array[index])
  while sum < invalid_number:
    number = int(file_array[index])
    sum += number
    if number <= min:
      min = number
    elif number >= max:
      max = number
    index += 1
  if sum == invalid_number:
    return max + min
  else:
    return 0

# Puzzle 1
for index, number in enumerate(file_array):
  if index < preamble_range:
    continue
  else:
    sum_array = form_sum_array(index)
    if int(number) in sum_array:
      continue
    else:
      invalid_number = int(number)
      break

# Puzzle 2
puzzle_2_value = 0
for index, number in enumerate(file_array):
  sum = find_number_set(index)
  if sum == 0:
    continue
  else:
    puzzle_2_value = sum
    break

print("Puzzle 1 solution: " + str(invalid_number))
print("Puzzle 2 solution: " + str(puzzle_2_value))