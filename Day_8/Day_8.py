import copy

file_array = []

# Read file into lines
with open('Day_8/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)

instruction_array = []
accumulator = 0

for instruction in file_array:
  instruction_array.append(instruction.split())

def loop_through_instructions(temp_instruction_array):
  global accumulator
  accumulator = 0
  index = 0
  traveled_indicies = []
  while index <= len(temp_instruction_array) - 1:
    # Check to see if we duplicated an instruction
    if index in traveled_indicies:
      return False
    else:
      traveled_indicies.append(index)

    # Break up the instruction
    instruction = temp_instruction_array[index]
    move = instruction[0]
    sign = instruction[1][0]
    if sign == "+":
      value = int(instruction[1][1:])
    elif sign == "-":
      value = -(int(instruction[1][1:]))

    # Handle the instruction logic
    if move == "jmp":
      index += value
    elif move == "acc":
      accumulator += value
      index += 1
    else:
      index += 1
  return True

# Puzzle 1
valid = loop_through_instructions(instruction_array)
print("Puzzle 1 solution: " + str(accumulator))

# Puzzle 2
for index, instruction in enumerate(instruction_array):
  temp_instruction_array = copy.deepcopy(instruction_array)
  if instruction[0] == "jmp":
    temp_instruction_array[index][0] = "nop"
  elif instruction[0] == "nop":
    temp_instruction_array[index][0] = "jmp"
  valid = loop_through_instructions(temp_instruction_array)
  if valid:
    break
print("Puzzle 2 solution: " + str(accumulator))