from functools import reduce
import re

file_array = []
strings = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open('Day_4/input.txt', 'r') as file:
  full_line = ""
  for line in file:
    if not line.isspace():
      full_line += line.replace("\n", " ")
    else:
      file_array.append(full_line)
      full_line = ""
 
# puzzle 1
valid_passports = 0

for passport in file_array:
  is_passport_valid = True
  for string in strings:
    if string not in passport:
      is_passport_valid = False
  if is_passport_valid:
    valid_passports += 1

# puzzle 2
valid_passports_2 = 0
eye_colors = "amb blu brn gry grn hzl oth"

def is_number(string, base):
  try:
    v = int(string, base)
    return True
  except ValueError:
    return False

def is_valid_height(string):
  valid = False
  if "cm" in string:
    value = int(re.findall(r'(.+)cm', string)[0])
    if value >= 150 and value <= 193:
      valid = True
  elif "in" in string:
    value = int(re.findall(r'(.+)in', string)[0])
    if value >= 59 and value <= 76:
      valid = True
  return valid

for passport in file_array:
  dictionary = {}
  is_passport_valid = True
  for string in strings:
    if string not in passport:
      is_passport_valid = False
      exit
    else:
      value = re.findall(r'{}:([^\s]+)'.format(string), passport)[0]
      if (string == "byr" and  not (int(value) <= 2002 and int(value) >= 1920)) \
        or (string == "iyr" and not (int(value) <= 2020 and int(value) >= 2010)) \
        or (string == "eyr" and not (int(value) <= 2030 and int(value) >= 2020)) \
        or (string == "hgt" and not is_valid_height(value)) \
        or (string == "hcl" and not (value[0] == "#" and is_number(value[1:6], 16))) \
        or (string == "ecl" and not (value in eye_colors)) \
        or (string == "pid" and not (is_number(value, 10) and len(value) == 9)):
        is_passport_valid = False
        exit

  if is_passport_valid:
    valid_passports_2 += 1

print("Puzzle 1 solution: " + str(valid_passports))
print("Puzzle 2 solution: " + str(valid_passports_2))


