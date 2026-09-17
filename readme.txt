### Logic & Data Structures
**Game Rules:**
* An alive cell survives if it has 2 or 3 alive neighbors; otherwise, it dies.
* A dead cell becomes alive if it has exactly 3 alive neighbors.
* **Grid:** 2D list (`Rows x Cols`) where `0` = dead, `1` = alive.
* **Tuple List:** List of `(row, col)` coordinate tuples for initial alive cells.

### Setup & Input
1. Initialize an empty grid (`Rows x Cols`) filled with `0`s.
2. Render the empty grid using `print_grid`.
3. Get `tuple_list` from user using `user_input`.
4. Validate boundaries with `check_coordinates(tuple_list)`:
   * Print an error and prompt again until all coordinates are valid.
5. Populate the grid with initial alive cells using `tuple_to_grid`.

### Main Loop
1. Display the current grid using `print_grid`.
2. Compute the next generation: `new_grid = game_logic(grid)`.
3. Update state: `grid = new_grid`.
4. Prompt user to continue or quit.
5. Break loop if the user quits.

--

### Functions

* **`user_input()`**
  1. Prompt user for space-separated coordinate pairs (`"row,col"`).
  2. Split input by spaces, then split each pair by comma into integers.
  3. Append `(x, y)` tuples to a list and return it.

* **`check_coordinates(my_list)`**
  1. Iterate over each `(x, y)` in `my_list`.
  2. Return `False` if any coordinate is out of bounds (`x < 0`, `x >= Rows`, `y < 0`, `y >= Cols`).
  3. Return `True` if all coordinates are within bounds.

* **`tuple_to_grid(grid, tuple_list)`**
  1. Iterate through `(r, c)` in `tuple_list`.
  2. Set `grid[r][c] = 1`.

* **`print_grid(grid)`**
  1. For each row, print the horizontal separator.
  2. Print cell borders (`|`) with `#` for alive cells and space for dead cells.
  3. Print the closing row border and final bottom separator.

* **`count_alive_neighbors(old_grid, r, c)`**
  1. Define 8 directional offsets: `[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]`.
  2. Iterate through offsets and ensure neighbor indices `(nr, nc)` are within grid bounds.
  3. Increment counter if `old_grid[nr][nc] == 1` and return the total.

* **`game_logic(old_grid)`**
  1. Create a `new_grid` of size `Rows x Cols` filled with `0`s.
  2. For each cell `(r, c)`:
     * Calculate `alive_neighbors = count_alive_neighbors(old_grid, r, c)`.
     * If cell is alive and has 2 or 3 neighbors: set `new_grid[r][c] = 1`.
     * If cell is dead and has exactly 3 neighbors: set `new_grid[r][c] = 1`.
  3. Return `new_grid`.