file_array = []
import math

# Read file into lines
with open('Day_5/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)

# Binary search to find the row/column
def binary_search(string, high, low):
  middle = (high + low) // 2
  if string[0] == "L" or string[0] == "F":
    if len(string) == 1:
      return low
    else:
      return binary_search(string[1:], middle, low)

  if string[0] == "R" or string[0] == "B":
    if len(string) == 1:
      return high
    else:
      return binary_search(string[1:], high, middle + 1)


########################################
# Puzzle 1
########################################
max_seat_id = 0

# Figure out all the seat IDs and track the highest
for boarding_pass in file_array:
  row_string = boarding_pass[0:7]
  column_string = boarding_pass[7:10]
  row = int(binary_search(row_string, 127, 0))
  column = int(binary_search(column_string, 7, 0))
  seat_id = (row * 8) + column
  if max_seat_id < seat_id:
    max_seat_id = seat_id


########################################
# Puzzle 2
########################################
my_seat = 0

# Add 1 to seat ids so we can start from 1 - x
seat_ids = [0] * (max_seat_id + 1)

# Populate the seat_ids array with all seat IDs
for boarding_pass in file_array:
  row_string = boarding_pass[0:7]
  column_string = boarding_pass[7:10]
  row = int(binary_search(row_string, 127, 0))
  column = int(binary_search(column_string, 7, 0))
  seat_id = (row * 8) + column
  seat_ids[seat_id] = 1

# Find the missing seat in the list
for index in range(max_seat_id):
  if seat_ids[index] == 0 and seat_ids[index-1] != 0 and seat_ids[index+1] != 0:
    my_seat = index



########################################
# Answers
########################################
print("Puzzle 1 solution: " + str(max_seat_id))
print("Puzzle 2 solution: " + str(my_seat))