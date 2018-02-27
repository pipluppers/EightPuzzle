# Search algorithm to solve the 8-puzzle

### Thanks to Dr. Eamonn Keogh for providing and overseeing this project.

Run the following commands to play the puzzle:
```
make
./start
```

The 8-puzzle game consists of a 3x3 board with 8 numbered tiles (1-8) and one blank tile. The goal of the game is to rearrange the board into the following configuration:

1 2 3

4 5 6

7 8

In order to solve the puzzle, this program will generate a search tree of the possible states. Given an initial state, this program will perform the search algorithm A* using one of three heuristics:
1. Uniform Cost Search
2. Misplaced Tile
3. Manhattan Distance

Heuristics offer the program the ability to choose the best path in the search tree given a state. The type of heuristic used is important when considering the performance of the program. The type of heuristic does not matter when the board is similar to the goal state, but when the board is completely different, the gap in performance between the heuristics becomes very significant. The ones used work as follows:
- Uniform Cost Search involves no heuristics. It simply chooses the path that costs the least. In terms of this search tree, all paths cost the same so this is essentially breadth-first search.
- Misplaced Tile heuristic counts the number of incorrect tiles. It chooses the path and expands the node with the least number of incorrect tiles.
- Manhattan Distance heuristic considers incorrect tiles and counts the total number of tiles they are from their desired location. This heuristic expands the node with the least number across all tiles.

The user may choose to use one of the given default puzzles or they are allowed to generate their own board. They may then choose their own heuristic and watch as the algorithm begins generating the states. Once the program is done running, the user may then view the statistics. They are as follows:
- Space Complexity: Maximum queue size
- Time Complexity: Number of nodes expanded
- Depth: Number of moves needed to solve the puzzle
