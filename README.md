Run the "Sudoku.py" file

Setup:
    A graphical window ("Sudoku") is created, displaying a Sudoku grid, title, and instructions.
    The starting puzzle is read from a file (startingPuzzle.txt), and a predefined solution (finishedPuzzle) is used for validation.
    
Rules:
    Each row, column, and 3x3 box must contain all of the numbers 1–9 
    No numbers can be repeated in any row, column, or 3x3 box 
    
Gameplay:
    Players use on-screen buttons (1–9) to fill the grid, updating it cell by cell.
    Inputs are stored in a 2D list (puzzle) and displayed on the grid in real-time.
    The "Check" button compares the player's input with the solution:
        If correct, a success message is shown, and the game closes.
        If incorrect, the game ends with a prompt to try again.

Features:
    A dynamic grid updates with user inputs.
    Validation ensures adherence to Sudoku rules, allowing players to check their completed puzzle.
   
