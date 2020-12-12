import copy

file_array = []

# Read file into lines
with open('Day_12/input.txt', 'r') as file:
  for line in file:
    file_array.append(line.strip())

# Puzzle 1
def rotate_ship(movement, direction):
  global headings
  global ship_heading
  if direction == "L":
    ship_heading = int((ship_heading - movement) % 4)
  elif direction == "R":
    ship_heading = int((ship_heading + movement) % 4)

headings = ["E", "S", "W", "N"]
ship_heading = 0
east_west = 0
north_south = 0
for instruction in file_array:
  direction = instruction[0]
  move = int(instruction[1:])
  if direction == "F":
    direction = headings[ship_heading]

  if direction == "E":
    east_west += move
  elif direction == "W":
    east_west -= move
  elif direction == "S":
    north_south -= move
  elif direction == "N":
    north_south += move
  elif direction == "L" or direction == "R":
    amount = move / 90
    rotate_ship(amount, direction)

print("Puzzle 1 solution: " + str(abs(east_west) + abs(north_south)))

# Puzzle 2
def rotate_waypoint(direction):
  global waypoint_pos
  temp = copy.deepcopy(waypoint_pos)
  if direction == "L":
    waypoint_pos[0] = temp[1]
    waypoint_pos[1] = temp[2]
    waypoint_pos[2] = temp[3]
    waypoint_pos[3] = temp[0]
  elif direction == "R":
    waypoint_pos[0] = temp[3]
    waypoint_pos[1] = temp[0]
    waypoint_pos[2] = temp[1]
    waypoint_pos[3] = temp[2]

headings = ["E", "S", "W", "N"]
ship_east_west = 0
ship_north_south = 0
waypoint_pos = [10, 0, 0, 1]
for instruction in file_array:
  direction = instruction[0]
  move = int(instruction[1:])
  if direction == "F":
    ship_east_west += waypoint_pos[0] * move
    ship_east_west -= waypoint_pos[2] * move
    ship_north_south += waypoint_pos[3] * move
    ship_north_south -= waypoint_pos[1] * move

  if direction == "E":
    waypoint_pos[0] += move
  elif direction == "W":
    waypoint_pos[2] += move
  elif direction == "S":
    waypoint_pos[1] += move
  elif direction == "N":
    waypoint_pos[3] += move
  elif direction == "L" or direction == "R":
    amount = move / 90
    for each in range(int(amount)):
      rotate_waypoint(direction)

print("Puzzle 2 solution: " + str(abs(ship_east_west) + abs(ship_north_south)))