# Conway's Game Of Life

A simulation of conway's game of life made in python language.  
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.  
One interacts with the Game of Life by creating an initial configuration and observing how it evolves.  
More information can be found at <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>.

### Rules Of Conway's Game Of Life

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead.  
Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.  

At each step in time, the following transitions occur:  
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.  
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Requirements

Python Language Interpreter, found at <https://www.python.org/>

Pygame - a python library for creating video games, found at <https://pyga.me/>

# Installation Instructions

Download and install the Python interpreter.  
Install the pygame library using pip.  
Run the "conway game of life.py" file using the python interpreter.  

# Playing
**Left Click** on a cell to make it a living cell.  
**Right Click** on a cell to make it a dead cell.  
Press **Space** key to start/stop the simulation.  
Press **A** key to turn all cells into living cells.  
Press **D** key to turn all cells into dead cells.  
Press **+** key while running the simulation to increase the speed of the simulation.  
Press **-** key while running the simulation to decrease the speed of the simulation.  
Press **0** key while running the simulation to run the simulation at the slowest setting.   
Press **1** key while running the simulation to run the simulation at the fastest setting.   
Press **Escape** key to quit.  