from sudokuBox import *
from buttons import *

win = GraphWin("Sudoku", 1000, 1000)

startingNumbers = [[0 for x in range(9)], [0 for y in range(9)]]
numList = open("startingPuzzle.txt", "r")
print(numList)

array2D = []
finishedPuzzle = [[7, 3, 8, 5, 1, 4, 6, 9, 2], [5, 2, 9, 3, 7, 6, 8, 4, 1], [4, 6, 1, 8, 9, 2, 5, 3, 7], [6, 8, 5, 7, 2, 9, 4, 1, 3], [2, 4, 7, 1, 6, 3, 9, 5, 8], [9, 1, 3, 4, 5, 8, 7, 2, 6], [3, 9, 4, 6, 8, 1, 2, 7, 5], [1, 5, 6, 2, 4, 7, 3, 8, 9], [8, 7, 2, 9, 3, 5, 1, 6, 4]]


for line in numList:
    array2D.append(line.split(","))

for i in range(9):
    for j in range(9):
        array2D[i][j] = array2D[i][j].strip()

title = Text(Point(250, 75), "Sudoku")
title.draw(win)

instructions = Text(Point(80,550), "Instructions:")
instructions.draw(win)

Ins1 = Text(Point(220,570), "Click the buttons to insert the corresponding number.")
Ins1.draw(win)

Ins2 = Text(Point(450,590), "The box being edited starts in the top left, and goes down each time you enter, then returns to the top on the next column.")
Ins2.draw(win)

Ins3 = Text(Point(195,610), "Please press the 'check' button when finished")
Ins3.draw(win)

# Drawing the Sudoku grid
for i in range(9):
    for j in range(9):
        box = SudokuBox(45, 45, 50 + i * 45, 100 + j * 45, array2D[i][j])
        box.drawBox(win)

# 1. Add 9 buttons each with different numbers
button1 = Button(win, Point(650, 200), 50, 50, "1")
button2 = Button(win, Point(710, 200), 50, 50, "2")
button3 = Button(win, Point(770, 200), 50, 50, "3")
button4 = Button(win, Point(650, 260), 50, 50, "4")
button5 = Button(win, Point(710, 260), 50, 50, "5")
button6 = Button(win, Point(770, 260), 50, 50, "6")
button7 = Button(win, Point(650, 320), 50, 50, "7")
button8 = Button(win, Point(710, 320), 50, 50, "8")
button9 = Button(win, Point(770, 320), 50, 50, "9")
buttonCheck = Button(win, Point(710, 400), 170, 75, "Check")

# 2. Make the button change the value in the first box
listOfNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = []  # Current row
puzzle = []  # Full puzzle

# Creates a grid so the numbers can be input onto the screen, with each spot being a space before being changed to whatever number is input by the button
textArray = [[None for _ in range(9)] for _ in range(9)]

# Function to update the grid with the number entered
def update_grid(i, j, num):
    # Create new text object if not already created
    text = Text(Point(50 + i * 45 + 22.5, 100 + j * 45 + 22.5 ), str(num))
    text.setSize(12)
    text.draw(win)
    textArray[i][j] = text  # Store the text object in the 2D array

# Main game loop
while True:
    # Wait for a mouse click
    clickedPoint = win.getMouse()

    # Extract x and y coordinates from the clickedPoint
    x = clickedPoint.getX()
    y = clickedPoint.getY()

    # Check if the click falls within a button

    if len(newList) == 9:
        # Move to the next row once 9 numbers are added
        puzzle.append(newList)
        newList = []  # Clear the current row for the next one

    # Button 1
    if 625 <= x <= 675 and 175 <= y <= 225:
        newList.append(listOfNums[0])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[0])

    # Button 2
    if 685 <= x <= 735 and 175 <= y <= 225:
        newList.append(listOfNums[1])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[1])

    # Button 3
    if 745 <= x <= 795 and 175 <= y <= 225:
        newList.append(listOfNums[2])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[2])

    # Button 4
    if 625 <= x <= 675 and 235 <= y <= 285:
        newList.append(listOfNums[3])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[3])

    # Button 5
    if 685 <= x <= 735 and 235 <= y <= 285:
        newList.append(listOfNums[4])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[4])

    # Button 6
    if 745 <= x <= 795 and 235 <= y <= 285:
        newList.append(listOfNums[5])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[5])

    # Button 7
    if 625 <= x <= 675 and 295 <= y <= 345:
        newList.append(listOfNums[6])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[6])

    # Button 8
    if 685 <= x <= 735 and 295 <= y <= 345:
        newList.append(listOfNums[7])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[7])

    # Button 9
    if 745 <= x <= 795 and 295 <= y <= 345:
        newList.append(listOfNums[8])
        update_grid(len(puzzle), len(newList) - 1, listOfNums[8])

    # If the puzzle is complete (9 rows filled), and hit check
    if len(puzzle) == 9:
        # If the puzzle is correct, it will show "Correct! Good Job!"
        if puzzle == finishedPuzzle:
            print("Correct! Good Job")
            win.close()
            break
        # If the puzzle is incorrect, it will show "Incorrect! Try Again!"
        elif puzzle != finishedPuzzle:
            print("Incorrect! Try Again!")
            win.close()
            break