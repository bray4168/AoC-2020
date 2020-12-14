file_array = []

# Read file into lines
with open('Day_13/input.txt', 'r') as file:
  for line in file:
    file_array.append(line.strip())

# Puzzle 1
time_stamp = int(file_array[0])
buses = file_array[1].split(",")
min = 999999
bus_used = 0
for bus in buses:
  if bus != "x":
    bus = int(bus)
    temp = time_stamp % bus
    temp = bus - temp
    if temp < min:
      min = temp
      bus_used = bus
print("Puzzle 1 solution: " + str(bus_used * min))

# Puzzle 2
buses = file_array[1].split(",")
time_stamp = 0
found = False
increment = int(buses[0])
start_index = 1
while found == False:
  time_stamp += increment
  for index in range(start_index, len(buses)):
    if buses[index] != "x":
      bus = int(buses[index])
      if ((time_stamp + index) % bus) == 0:
        found = True
        increment *= int(buses[index])
        start_index = index + 1
      else:
        found = False
        break
print("Puzzle 2 solution: " + str(time_stamp))
