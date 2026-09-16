logic:
- if the cell is alive, it stays alive if it has 2 or 3 alive neighbors; otherwise it dies
- if the cell is dead, it becomes alive if it has exactly 3 alive neighbors
- grid: list of lists representing cell states (0 = dead, 1 = alive)
- tuple list: list of (row, col) coordinates entered by the user

setup and input:
1. create grid filled with 0s of size (Rows x Cols)
2. print empty grid using print_grid
3. get tuple_list from user using user_input
4. while check_coordinates(tuple_list) is False:
     print error message
     get tuple_list again using user_input
5. update grid with initial alive cells using tuple_to_grid

main loop:
1. print current grid using print_grid
2. calculate next generation: new_grid = game_logic(grid)
3. update grid: grid = new_grid
4. ask user for input to continue or quit
5. if quit: stop the loop

func - user_input:
1. initialize empty list my_list
2. prompt user to enter coordinates "row,col" separated by spaces
3. split input string by spaces into coordinate pairs
4. for each pair:
     split by comma into x and y
     convert x and y to integers
     append (x, y) tuple to my_list
5. return my_list

func - check_coordinates:
1. accept: my_list of tuples
2. for each (x, y) in my_list:
     if x < 0 or x >= Rows or y < 0 or y >= Cols:
       return False
3. return True if all coordinates are within bounds

func - print_grid:
1. accept: grid
2. for each row in Rows:
     print separator line
     for each col in Cols:
       print cell wall "|"
       if grid[row][col] == 1: print "#"
       else: print space
     print final "|" to close the row
3. print final separator line

func - tuple_to_grid:
1. accept: grid, tuple_list
2. for each (r, c) in tuple_list:
     set grid[r][c] = 1

func - game_logic:
1. accept: old_grid, returns: new_grid
2. create new_grid of size (Rows x Cols) filled with 0s
3. for each row r from 0 to Rows - 1:
     for each col c from 0 to Cols - 1:
       alive_neighbors = count_alive_neighbors(old_grid, r, c)

       if old_grid[r][c] == 1:
         if alive_neighbors == 2 or alive_neighbors == 3:
           new_grid[r][c] = 1
       else:
         if alive_neighbors == 3:
           new_grid[r][c] = 1
4. return new_grid

func - count_alive_neighbors:
1. accept: old_grid, cell coordinates (r, c), returns: count
2. define 8 direction offsets: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
3. counter = 0
4. for each (dr, dc) in offsets:
     nr = r + dr
     nc = c + dc
     if 0 <= nr < Rows and 0 <= nc < Cols:
       if old_grid[nr][nc] == 1:
         counter = counter + 1
5. return counter