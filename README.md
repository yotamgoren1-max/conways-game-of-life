# 🧬 Conway's Game of Life

A modular, terminal-based simulation of Conway's Game of Life built from scratch in Python. This project demonstrates core concepts of cellular automata, synchronous discrete 2D matrix state transitions, Moore neighborhood algorithms, and CLI input parsing.

## 🚀 Features

* **Standard Conway Rules (B3/S23):** Fully implements classic survival, death, and reproduction transition conditions.
* **Moore Neighborhood Evaluation:** Accurately calculates 8 adjacent neighbor states with strict grid boundary bounds-checking.
* **Dynamic Coordinate Seeding:** Flexible CLI parser that ingests space-separated coordinate pairs with real-time input validation.
* **ASCII Grid Visualization:** Clean terminal rendering displaying bounding borders and active cells dynamically.
* **Modular Codebase:** Strict separation of concerns between global parameters, algorithmic functions, and the runtime loop.

## 📁 Project Structure

* `main.py`: The entry point managing the core execution loop, user progression, and game termination conditions.
* `game_func.py`: Pure helper functions handling matrix generation, state calculation, coordinate validation, and ASCII rendering.
* `config.py`: Centralized configuration file defining grid dimensions (`Rows`, `Cols`) and display formatting, eliminating "magic numbers".

## 🧠 Architecture & Logic Flow

### Logic & Data Structures
* **Game Rules:**
  * An alive cell survives if it has 2 or 3 alive neighbors; otherwise, it dies.
  * A dead cell becomes alive if it has exactly 3 alive neighbors.
* **Grid:** 2D list (`Rows x Cols`) where `0` represents a dead cell and `1` represents an alive cell.
* **Tuple List:** List of `(row, col)` coordinate tuples for initial alive cells.

### Setup & Input
1. Initialize an empty grid (`Rows x Cols`) populated with `0`s.
2. Render the empty grid using `print_grid`.
3. Read raw coordinates into `tuple_list` via `user_input`.
4. Validate coordinates with `check_coordinates(tuple_list)`:
   * Re-prompt on invalid or out-of-bounds input until valid.
5. Populate initial alive cells into the grid using `tuple_to_grid`.

### Main Loop
1. Display the current grid state using `print_grid`.
2. Compute the next generation: `new_grid = game_logic(grid)`.
3. Update state: `grid = new_grid`.
4. Check termination condition (`is_over` returns `True` if all cells are dead).
5. Prompt user to press Enter to advance or enter any key to quit.

---

### Functions

* **`user_input()`**
  * Prompts for space-separated `"row,col"` coordinates.
  * Parses tokens, adjusts for 0-based indexing, and returns a list of `(x, y)` tuples.

* **`check_coordinates(my_list)`**
  * Verifies every `(x, y)` tuple satisfies $0 \le x < \text{Rows}$ and $0 \le y < \text{Cols}$.
  * Returns `True` if all coordinates are within bounds, otherwise `False`.

* **`tuple_to_grid(grid, tuple_list)`**
  * Updates the grid in-place by setting `grid[x][y] = 1` for all initial active cells.

* **`print_grid(grid)`**
  * Prints formatted horizontal lines and vertical borders (`|`).
  * Displays `#` for alive cells and empty spaces for dead cells.

* **`count_alive_neighbors(grid, r, c)`**
  * Iterates across 8 directional offsets (Moore neighborhood).
  * Safely counts adjacent alive cells while ignoring out-of-bounds queries.

* **`game_logic(grid)`**
  * Allocates a new empty grid matrix of dimensions `Rows x Cols`.
  * Computes neighbor counts for each cell and applies Conway's state transition rules synchronously.
  * Returns the newly generated state matrix.

* **`is_over(grid)`**
  * Scans the grid and returns `True` if all cells are dead (`0`), ending the simulation.
