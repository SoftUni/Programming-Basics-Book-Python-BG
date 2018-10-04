#
# Problem 1
#

tribonacci_first = int(input())
tribonacci_second = int(input())
tribonacci_third = int(input())

spiral_current = int(input())
spiral_step = int(input())

# Trbonacci
tribonacci_numbers = [tribonacci_first,
                      tribonacci_second,
                      tribonacci_third]

tribonacci_current = tribonacci_third
while tribonacci_current < 1000000:
    tribonacci_current = tribonacci_first + \
                         tribonacci_second + \
                         tribonacci_third
    tribonacci_numbers.append(tribonacci_current)

    tribonacci_first = tribonacci_second
    tribonacci_second = tribonacci_third
    tribonacci_third = tribonacci_current

# Spiral
spiral_numbers = [spiral_current]
spiral_count = 0
spiral_step_mul = 1
while spiral_current < 1000000:
    spiral_current += spiral_step * spiral_step_mul
    spiral_numbers.append(spiral_current)
    spiral_count += 1
    if spiral_count % 2 == 0:
        spiral_step_mul += 1

# Find answer
found = False
for i in range(0, len(tribonacci_numbers)):
    for j in range(0, len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j] \
                and tribonacci_numbers[i] <= 1000000:
            print(tribonacci_numbers[i])
            found = True
            break
    if found:
        break

if not found:
    print("No")

# Faster implementation:
# while tribonacci_current <= 1000000 and spiral_current <= 1000000:
#     if tribonacci_current == spiral_current:
#         print("TODO: Print and stop execution")
#     elif tribonacci_current < spiral_current:
#         print("TODO: Generate next Tribonacci number")
#     else:
#         print("TODO: Generate next Spiral number")


#
# Problem 2
#

from datetime import date as datetype
from datetime import timedelta
from math import floor

first_year = int(input())
second_year = int(input())
number_to_search_for = int(input())

date = datetype(first_year, 1, 1)
found = False

while date.year <= second_year:
    d1 = floor(date.day / 10)  # First day digit
    d2 = date.day % 10  # Second day digit

    d3 = floor(date.month / 10)  # First month digit
    d4 = date.month % 10  # Second month digit

    d5 = floor(date.year / 1000)  # First year digit
    d6 = floor(date.year / 100) % 10  # Second year digit
    d7 = floor(date.year / 10) % 10  # Third year digit
    d8 = date.year % 10  # Fourth year digit

    weight = d1 * (d2 + d3 + d4 + d5 + d6 + d7 + d8) + \
             d2 * (d3 + d4 + d5 + d6 + d7 + d8) + \
             d3 * (d4 + d5 + d6 + d7 + d8) + \
             d4 * (d5 + d6 + d7 + d8) + \
             d5 * (d6 + d7 + d8) + \
             d6 * (d7 + d8) + \
             d7 * d8

    if weight == number_to_search_for:
        print(str(d1) + str(d2) + "-" + str(d3) + str(d4) +
              "-" + str(d5) + str(d6) + str(d7) + str(d8))
        found = True
    date = date + timedelta(days=1)

if not found:
    print("No")


#
# Problem 3
#

first_number = int(input())
second_number = int(input())

pattern = "abcde"
result = ""

for i1 in range(0, 5):
    for i2 in range(0, 5):
        for i3 in range(0, 5):
            for i4 in range(0, 5):
                for i5 in range(0, 5):
                    full_word = pattern[i1] + \
                                pattern[i2] + \
                                pattern[i3] + \
                                pattern[i4] + \
                                pattern[i5]

                    word = pattern[i1]

                    if word.find(pattern[i2]) == -1:
                        word += pattern[i2]
                    if word.find(pattern[i3]) == -1:
                        word += pattern[i3]
                    if word.find(pattern[i4]) == -1:
                        word += pattern[i4]
                    if word.find(pattern[i5]) == -1:
                        word += pattern[i5]

                    weight = 0
                    for i in range(0, len(word)):
                        multiplier = 0
                        if word[i] == 'a':
                            multiplier = 5
                        if word[i] == 'b':
                            multiplier = -12
                        if word[i] == 'c':
                            multiplier = 47
                        if word[i] == 'd':
                            multiplier = 7
                        if word[i] == 'e':
                            multiplier = -32
                        weight += multiplier * (i + 1)

                    if first_number <= weight <= second_number:
                        result += full_word + " "

if result == "":
    print("No")
else:
    print(result.strip())
