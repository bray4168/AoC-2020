file_array = []

# Read file into lines
with open('Day_10/input.txt', 'r') as file:
  for line in file:
    file_array.append(int(line.strip()))
file_array.sort()

# Puzzle 1
check_voltage = 0
diff_1 = 0
diff_3 = 1 # start with 1 for the difference from device
for voltage in file_array:
  difference = voltage - check_voltage
  check_voltage = voltage
  if difference == 1:
    diff_1 += 1
  elif difference == 3:
    diff_3 += 1

# Puzzle 2
sum_array = [0] * len(file_array)
index = len(file_array) - 1
while index >= 0:
  temp_sum = 0
  voltage = file_array[index]
  if index + 1 == len(file_array):
    sum_array[index] = 1
    index -= 1
    continue
  if index + 1 < len(file_array):
    if file_array[index + 1] - voltage <= 3:
      temp_sum += sum_array[index + 1]
  if index + 2 < len(file_array):
    if file_array[index + 2] - voltage <= 3:
      temp_sum += sum_array[index + 2]
  if index + 3 < len(file_array):
    if file_array[index + 3] - voltage <= 3:
      temp_sum += sum_array[index + 3]
  sum_array[index] = temp_sum
  index -= 1

# Print solutions
print("Puzzle 1 solution: " + str(diff_1 * diff_3))
print("Puzzle 2 solution: " + str(sum_array[0] + sum_array[1]))