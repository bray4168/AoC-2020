file_array = []
import copy

# Read file into lines
with open('Day_11/input.txt', 'r') as file:
  for line in file:
    file_array.append(list(line.strip()))

def get_adjacent_seats(array_index, string_index):
  adjacent_seats = [
    [array_index + 1, string_index],
    [array_index - 1, string_index],
    [array_index, string_index + 1],
    [array_index, string_index - 1],
    [array_index + 1, string_index + 1],
    [array_index + 1, string_index - 1],
    [array_index - 1, string_index + 1],
    [array_index - 1, string_index - 1],
  ]
  indexes_to_delete = []
  for each in adjacent_seats:
    if each[0] < 0 or each[0] > len(file_array) - 1:
      indexes_to_delete.append(each)
    elif each[1] < 0 or each[1] > len(file_array[array_index]) - 1:
      indexes_to_delete.append(each)
  for each in indexes_to_delete:
    adjacent_seats.remove(each)
  return adjacent_seats

def modified_get_adjacent_seats(array_index, string_index):
  adjacent_seats = [None] * 8
  for count in range(1, len(file_array[0])):
    # search vertical
    if array_index + count < len(file_array) and adjacent_seats[0] == None:
      if file_array[array_index + count][string_index] == "#" or file_array[array_index + count][string_index] == "L":
        adjacent_seats[0] = [array_index + count, string_index]
    if array_index - count >= 0 and adjacent_seats[1] == None:
      if file_array[array_index - count][string_index] == "#" or file_array[array_index - count][string_index] == "L":
        adjacent_seats[1] = [array_index - count, string_index]
    # search horizontal
    if string_index + count < len(file_array[0]) and adjacent_seats[2] == None:
      if file_array[array_index][string_index + count] == "#" or file_array[array_index][string_index + count] == "L":
        adjacent_seats[2] = [array_index, string_index + count]
    if string_index - count >= 0 and adjacent_seats[3] == None:
      if file_array[array_index][string_index - count] == "#" or file_array[array_index][string_index - count] == "L":
        adjacent_seats[3] = [array_index, string_index - count]
    # search diagonals
    if array_index + count < len(file_array) and string_index + count < len(file_array[0]) and adjacent_seats[4] == None:
      if file_array[array_index + count][string_index + count] == "#" or file_array[array_index + count][string_index + count] == "L":
        adjacent_seats[4] = [array_index + count, string_index + count]
    if array_index - count >= 0 and string_index + count < len(file_array[0]) and adjacent_seats[5] == None:
      if file_array[array_index - count][string_index + count] == "#" or file_array[array_index - count][string_index + count] == "L":
        adjacent_seats[5] = [array_index - count, string_index + count]
    if array_index + count < len(file_array) and string_index - count >= 0 and adjacent_seats[6] == None:
      if file_array[array_index + count][string_index - count] == "#" or file_array[array_index + count][string_index - count] == "L":
        adjacent_seats[6] = [array_index + count, string_index - count]
    if array_index - count >= 0 and string_index - count >= 0 and adjacent_seats[7] == None:
      if file_array[array_index - count][string_index - count] == "#" or file_array[array_index - count][string_index - count] == "L":
        adjacent_seats[7] = [array_index - count, string_index - count]
  # remove None
  while True:
    if None in adjacent_seats:
      adjacent_seats.remove(None)
    else:
      break
  return adjacent_seats

def modify_seats(adjacent_seat_type = False):
  temp_array = copy.deepcopy(file_array)
  for i in range(len(file_array)):
    for j in range(len(file_array[i])):
      if file_array[i][j] == ".":
        continue
      else:
        if adjacent_seat_type == False:
          adjacent_seats = get_adjacent_seats(i, j)
          seats = 4
        else:
          adjacent_seats = modified_get_adjacent_seats(i,j)
          seats = 5
        occupied_seats = 0
        for seat in adjacent_seats:
          if file_array[seat[0]][seat[1]] == "#":
            occupied_seats += 1
        if file_array[i][j] == "L":
          if occupied_seats == 0:
            temp_array[i][j] = "#"
        elif file_array[i][j] == "#":
          if occupied_seats >= seats:
            temp_array[i][j] = "L"
  return temp_array

def count_occupied_seats():
  occupied_seats = 0
  for each in file_array:
    occupied_seats += each.count("#")
  return occupied_seats

# Puzzle 1
while True:
  temp_array = modify_seats()
  if file_array == temp_array:
    print("Puzzle 1 solution: " + str(count_occupied_seats()))
    break
  else:
    file_array = copy.deepcopy(temp_array)

file_array = []
# Read file into lines
with open('Day_11/input.txt', 'r') as file:
  for line in file:
    file_array.append(list(line.strip()))
      
# Puzzle 2
while True:
  temp_array = modify_seats(True)
  if file_array == temp_array:
    print("Puzzle 2 solution: " + str(count_occupied_seats()))
    break
  else:
    file_array = copy.deepcopy(temp_array)



