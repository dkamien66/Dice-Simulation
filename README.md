### Dice-Simulation
# What
This project is about simulating dice rolls and displaying the outcome in the terminal. The project template is from Real Python "Build a Dice-Rolling Application With Python" https://realpython.com/python-dice-roll/. 

# Why
This was one of my first projects in Python as I was learning it. After finishing the template, I added my own extensions to the project: more die choices (7-9) and unlimited dice outcomes. I found a problem in which no more than fifteen dice could be clearly displayed in the terminal. This was because the program would print all the dice outcomes on one row. I modified the code that generates and displays the ASCII diagram of the dice faces so that several rows were allowed that prevented cluttering of the dice faces on the screen.

# How it works
The user is asked how many dice they want to roll and what sided dice they want them to be. User input validation occurs. Dice are randomly rolled. The dice faces to display are obtained in a new list from the list of random rolls, and this is done using a dictionary of the keys being 1 to 9 and the values being the corresponding ASCII dice diagram.

Now getting the string of the outcomes. 
The list of dice faces is split into row groupings of 10; the leftover are in the last row. Iterating over each row grouping, we iterate over another for loop five times, combining each row of a dice face and appending to a list, always checking that the quantity per row is never over ten or over the total number of dice. After iterating over all row groupings, the list is returned.
Finally, a RESULTS header and each element of the list, a row of a row of dice faces (yes a row of a row), are all concatenated together to return this string.
