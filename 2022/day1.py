# --- Day 1: Calorie Counting ---

# Put these values in a list.
# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:
# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
# The second Elf is carrying one food item with 4000 Calories.
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
# The fifth Elf is carrying one food item with 10000 Calories.

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

import os

def get_calories_per_elf(calories_file):
    calories = 0
    elves = []

    for line in calories_file:
        try:
            calories += int(line)
            continue
        except:
            elves.append(calories)
            calories = 0

    elves.append(calories) # To get last line in file
    return elves

def get_elf_with_most_calories(calories):
    max_value = calories[0]
    index = 0

    for i in range(1, len(calories)):
        if calories[i] > max_value:
            max_value = calories[i]
            index = i
    
    return index + 1

def main():
    current_directory = os.getcwd()
    current_directory += "\calories.txt"
    file = open(current_directory)
    
    calories_list = get_calories_per_elf(file)

    print("The elf with most calories is elf number: %d." % get_elf_with_most_calories(calories_list))

    # Now sort list and find out how much that elf is carrying.
    calories_list.sort(reverse=True)
    print("The elf with most calories is carrying: %d calories." % (calories_list[0]))

if __name__ == "__main__":
    main()