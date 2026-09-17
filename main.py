import config
import game_func

# Initialize an empty grid
grid=[]
for i in range (config.Rows):
    row=[0]*config.Cols
    grid.append(row)

# Get and validate initial cell coordinates from the user
tuple_list = game_func.user_input()
while not game_func.check_coordinates(tuple_list):
    print("Invalid coordinates, please re-enter.")
    tuple_list = game_func.user_input()

# Populate the grid with initial live cells
game_func.tuple_to_grid(grid, tuple_list)

# Main simulation loop
game_running = True
while game_running:
    game_func.print_grid(grid)
    grid = game_func.game_logic(grid)
    # Check if all cells died
    if game_func.is_over(grid):
        print("All the cells are dead, Thanks for playing!")
        game_func.print_grid(grid)
        game_running = False
    else:
        # Prompt user to advance generation or quit
        user_choice = input("Press Enter to continue, or any other key + Enter to quit: ")
        if user_choice != "":
            print("Thanks for playing!")
            game_running = False