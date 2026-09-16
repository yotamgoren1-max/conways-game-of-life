import time
import config
import game_func
grid=[]
for i in range (config.Rows):
    row=[0]*config.Cols
    grid.append(row)
game_func.print_grid(grid)
tuple_list=game_func.user_input()
while not game_func.check_coordinates(tuple_list):
    print("invalid coordinates please renter")
    tuple_list=game_func.user_input()





