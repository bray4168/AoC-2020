file_array = []
array = []
correct_count = 0
correct_count_2 = 0

with open('Day_2/input.txt', 'r') as file:
  for line in file:
    file_array.append(line)

# puzzle 1
for line in file_array:
  letter_count = 0
  array = line.split(' ')
  min = int(array[0].split("-")[0])
  max = int(array[0].split("-")[1])
  letter = array[1][0]
  word = array[2].rstrip()
  for each in word:
    if each == letter:
      letter_count += 1
  if letter_count >= min and letter_count <= max:
    correct_count += 1

#puzzle 2
for line in file_array:
  array = line.split(' ')
  index_1 = int(array[0].split("-")[0]) - 1
  index_2 = int(array[0].split("-")[1]) - 1
  letter = array[1][0]
  word = array[2].rstrip()
  print(word, letter, index_1, index_2)
  if (word[index_1] == letter and not word[index_2] == letter) or (not word[index_1] == letter and word[index_2] == letter):
    correct_count_2 += 1

print("Puzzle 1 solution is: " + str(correct_count))
print("Puzzle 2 solution is: " + str(correct_count_2))



