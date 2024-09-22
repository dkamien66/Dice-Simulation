"""
Followed from https://realpython.com/python-dice-roll/
Added:
    Up to 9 sided dice
    Support for any number of dice
        Modified code that generates and displays the ASCII diagram of dice faces so several rows are allowed that prevents cluttering of the screen
"""

import random

"""Main application"""
def main():
    while True:
        # 1. Get user input on how many dice rolls
        dice_input = input("How many dice do you wish to roll? [q to quit]: ")
        if dice_input == "q":
            raise SystemExit
        else:
            # 2. Validate user input for dice
            num_dice = validate_dice_input(dice_input.strip())
            # 3. Get user inpput on how many sides each die has
            sides_input = input("How many sides are on each die? [1-9]: ")
            # 4. Validate user input for sides
            num_sides = validate_sides_input(sides_input.strip())
            # 5. Obtain random rolls
            dice_array = roll_dice(num_dice, num_sides)
            # 6. Obtain ASCII dice diagram
            dice_diagram = generate_dice_faces(dice_array)
            print(f"\n{dice_diagram}")

"""Checks that user has typed an integer. Returns the input as an int."""
def validate_dice_input(input):
    # if the user's input is an int, then it's a valid number and should be returned as an int
    try:
        num = int(input)
    except ValueError:
        print("You must type an integer!")
        raise SystemExit
    else:
        return num
    
def validate_sides_input(input):
    # if the user's inpnut is in the set of ints 1 to 9, it's valid and should be returned as an int
    if input in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        return int(input)
    else:
        print("Number of sides must be between 1 and 9!")
        raise SystemExit
    
"""Given the user inputted number, rolls that many random dice and returns results in a list."""
def roll_dice(dice, sides):
    dice_results = []
    for _ in range(dice):
        # returns a number from 1 to sides chosen by the user (inclusive)
        roll = random.randint(1, sides)
        dice_results.append(roll)
    return dice_results
    
"""Dictionary for dice face values"""
DICE_ART_DICT = {
    1: (
        "┌───────r─┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    7: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    8: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
    9: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART_DICT[1]) # How many rows = 5
DIE_WIDTH = len(DICE_ART_DICT[1][0]) # How many columns = 11
DIE_FACE_SEPARATOR = " "

"""Uses the random dice rolls to generate an ASCII diagram of them, and returns a string of this result."""
def generate_dice_faces(dice_results):
    dice_faces = get_dice_faces(dice_results)
    dice_faces_rows = get_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    # Concatenate the RESULTS header with the rows of the diagram of dice faces
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

"""Helper method for generating the ASCII dice faces."""
def get_dice_faces(dice_results):
    # Generate a list of dice faces using DICE_ART from the users random dice rolls
    dice_faces = []
    for value in dice_results:
        dice_faces.append(DICE_ART_DICT[value])
    return dice_faces

"""Helper method for creating the list of rows to be printed"""
def get_dice_faces_rows(dice_faces):
    # Generate a list containing the rows of the diagram of dice faces to be returned and printed
    dice_faces_rows = [] 

    num_row_groupings = ((len(dice_faces) - 1) // 10) + 1 # splits dice faces 10 per row e.g. 15 dice faces = 10 on the first row, 5 on the second row
    
    # which grouping row these dice faces will be in
    for grouping_row in range(num_row_groupings):
        # which row of each dice face [0 to 4] we are using
        for row_idx in range(DIE_HEIGHT):
            row_components = []

            # which die number we are iterating through (can be the max of 10 per row, or whatever is left over on the last row)
            die_idx = 0
            while die_idx < 10 and grouping_row*10+die_idx < len(dice_faces):
                row_components.append(dice_faces[grouping_row*10+die_idx][row_idx])
                die_idx += 1
            
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)
    
    return dice_faces_rows

main()