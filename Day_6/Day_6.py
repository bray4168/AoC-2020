import re

file_array = []

# Read all groups of lines into one string
with open('Day_6/input.txt', 'r') as file:
  full_line = ""
  for line in file:
    if not line.isspace():
      full_line += line.replace("\n", " ")
    else:
      file_array.append(full_line)
      full_line = ""
  file_array.append(full_line)

# Puzzle 1
# Loop through each string and remove duplicate letters
# then it leaves you with the count for each string
sum = 0
for each in file_array:
  each = each.replace(" ", "")
  for char in each:
    count = each.count(char)
    each = each.replace(char, "", count - 1)
  sum += len(each)

# Puzzle 2
sum_2 = 0
for each in file_array:
  # Seperate each string into the first person and then
  # the rest of the people
  each = each.rstrip()
  number_in_group = each.count(" ") + 1
  each = each.split(" ", 1)

  # If only one in group then all are valid
  # else check that everyone matches
  if number_in_group == 1:
    sum_2 += len(each[0])
  else:
    for char in each[0]:
      count = each[1].count(char) + 1
      if count == number_in_group:
        sum_2 += 1

# Solutions
print("Puzzle 1 solution: " + str(sum))
print("Puzzle 2 solution: " + str(sum_2))