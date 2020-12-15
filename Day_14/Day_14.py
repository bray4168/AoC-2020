import re

file_array = []

# Read file into lines
with open('Day_14/input.txt', 'r') as file:
  for line in file:
    file_array.append(line.strip())

# Puzzle 1
# Apply the mask to an integer and return the new int
def apply_mask(number):
  mask_length = 36
  bit_string = ""
  bit_array = ["0"] * mask_length
  temp_bit_array = bin(number)
  for index in range(1, 37):
    if temp_bit_array[-index] == "b":
      break
    else:
      bit_array[-index] = temp_bit_array[-index]
  for index, bit in enumerate(mask):
    if bit != "X":
      bit_array[index] = bit
  bit_string = bit_string.join(bit_array)
  return int(bit_string, 2)

# Loop through the text input and perform actions needed
memory_map = {}
bit_mask = ""
sum = 0
for line in file_array:
  if "mask" in line:
    mask = line.split("= ")[1]
  elif "mem" in line:
    values = re.findall(r'.+\[(.*)\].+= (.*)', line)
    address = values[0][0]
    value = values[0][1]
    memory_map[address] = apply_mask(int(value))

# Sum all the memory entries
for key, value in memory_map.items():
  sum += int(value)

print("Puzzle 1 solution: " + str(sum))

# Puzzle 2
# Apply the mask to the address and return the new address string
def apply_mask(number):
  mask_length = 36
  bit_string = ""
  bit_array = ["0"] * mask_length
  temp_bit_array = bin(number)
  for index in range(1, 37):
    if temp_bit_array[-index] == "b":
      break
    else:
      bit_array[-index] = temp_bit_array[-index]
  for index, bit in enumerate(mask):
    if bit != "0":
      bit_array[index] = bit
  bit_string = bit_string.join(bit_array)
  return bit_string

# we can simply keep an int count and apply the bit of it to the range of X's
# I.E, for two x's we have 00, 01, 10, 11 which is int 1-4
def get_addresses(address_string):
  mask_length = 36
  floats = address_string.count("X")
  addresses = []
  for address in range(2**floats):
    temp = list(address_string)
    count = bin(address)[2:]
    count = count.rjust(mask_length, "0")
    for each in range(1, floats + 1):
      index = temp.index("X")
      temp[index] = count[-each]
    addresses.append("".join(temp))
  return addresses

# Loop through the input but apply multiple addresses for each write
memory_map = {}
bit_mask = ""
sum = 0
for line in file_array:
  if "mask" in line:
    mask = line.split("= ")[1]
  elif "mem" in line:
    values = re.findall(r'.+\[(.*)\].+= (.*)', line)
    address = values[0][0]
    value = values[0][1]
    address_string = apply_mask(int(address))
    addresses = get_addresses(address_string)
    for address in addresses:
      memory_map[address] = value

# Sum all the memory entries
for key, value in memory_map.items():
  sum += int(value)

print("Puzzle 2 solution: " + str(sum))