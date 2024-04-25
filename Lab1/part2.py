# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.

arr = [1, 2, 3, 3, 3]
arr = list(set(arr))
print(arr)

# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.


def merge_halves(a, b):
    """Merges two strings by combining their front and back halves."""
    a_mid = len(a) // 2 + len(a) % 2
    b_mid = len(b) // 2
    return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]


# Example usage
string1 = "abcd"
string2 = "efgh"
merged_string = merge_halves(string1, string2)
print(merged_string)  # Output: abefcdgh


# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False


def all_unique(nums):
    """Checks if all numbers in a sequence are unique."""
    return len(set(nums)) == len(
        nums
    )  # Compare the lengths of the original list and the set created from it


# Example usage
numbers1 = [1, 5, 7, 9]
numbers2 = [2, 4, 5, 5, 7, 9]
print(all_unique(numbers1))  # Output: True
print(all_unique(numbers2))  # Output: False


# 4- Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)


def bubble_sort(nums):
    """Sorts a list of numbers using bubble sort algorithm."""
    n = len(nums)
    for i in range(n - 1):  # Iterate through the list n-1 times
        for j in range(n - i - 1):  # Compare adjacent elements
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # Swap elements if they are not in order


# Example usage
numbers = [5, 3, 8, 6, 7, 2]
bubble_sort(numbers)
print(numbers)  # Output: [2, 3, 5, 6, 7, 8]


# 5- Gusses game

import random


def guess_game():
    """Implements a number guessing game with 10 tries."""
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    tries = 10
    guessed_numbers = set()

    while tries > 0:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Number out of range. Please try again.")
            continue

        if user_guess in guessed_numbers:
            print("You already guessed that number. Try again.")
            continue

        guessed_numbers.add(user_guess)
        tries -= 1

        if user_guess == random_number:
            print("Congratulations! You guessed the number in", 10 - tries, "tries!")
            if input("Play again? (y/n): ").lower() == "y":
                guess_game()  # Start a new game
            else:
                print("Thanks for playing!")
                break  # Exit the game
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    if tries == 0:
        print("You ran out of tries. The number was", random_number)
        if input("Play again? (y/n): ").lower() == "y":
            guess_game()  # Start a new game
        else:
            print("Thanks for playing!")


# Start the game
guess_game()
