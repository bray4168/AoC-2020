file_array = []
import re

# Read file into lines
with open('Day_7/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)

bag_map = {}
bag_to_search = "shiny gold"
end_bag = "no other"

def build_bag_map(strings):
  for string in strings:
    values = re.findall(r'(^|\d)(.+?)bag', string)
    colors = []
    numbers = []
    for each in values:
      colors.append(each[1].strip())
      numbers.append(each[0].strip())
    if end_bag in string:
      bag_map[colors[0]] = {"no other": 1}
    else:
      map = {}
      for index in range(len(colors[1:])):
       map[colors[index + 1]] = numbers[index + 1]
      bag_map[colors[0]] = map
  return

def check_bag_recursive(bag_color):
  for bag in bag_map[bag_color]:
    if bag == end_bag:
      return False
    elif bag == bag_to_search:
      return True
    else:
      if check_bag_recursive(bag):
        return True

def sum_bag_recursive(bag_color):
  sum = 0
  for bag, count in bag_map[bag_color].items():
    if bag == end_bag:
      sum += 0
    else:
      sum += int(count) + (int(count) * sum_bag_recursive(bag))
  return sum

# Puzzle 1
sum = 0
build_bag_map(file_array)
for bag in bag_map:
  if check_bag_recursive(bag):
    sum += 1

# Puzzle 2
build_bag_map(file_array)
sum_2 = sum_bag_recursive(bag_to_search)

# Print solutions
print("Puzzle 1 solution: " + str(sum))
print("Puzzle 1 solution: " + str(sum_2))
  