file_array = []
import math

with open('Day_5/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)

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

# puzzle 1
max_seat_id = 0

for boarding_pass in file_array:
  row_string = boarding_pass[0:7]
  column_string = boarding_pass[7:10]
  row = int(binary_search(row_string, 127, 0))
  column = int(binary_search(column_string, 7, 0))
  seat_id = (row * 8) + column
  if max_seat_id < seat_id:
    max_seat_id = seat_id

# puzzle 2
my_seat = 0
seat_ids = [0] * max_seat_id
for boarding_pass in file_array:
  row_string = boarding_pass[0:7]
  column_string = boarding_pass[7:10]
  row = int(binary_search(row_string, 127, 0))
  column = int(binary_search(column_string, 7, 0))
  seat_id = (row * 8) + column
  seat_ids[seat_id - 1] = 1

for index in range(max_seat_id):
  if seat_ids[index] == 0 and seat_ids[index-1] != 0 and seat_ids[index+1] != 0:
    my_seat = index + 1



print("Puzzle 1 solution: " + str(max_seat_id))
print("Puzzle 2 solution: " + str(my_seat))