import config
def print_grid(grid):
    for i in range (config.Rows):
        print (config.separator) #print separator lines
        for j in range (config.Cols):
            print("| " , end="")
            if grid[i][j]==1:
                print ("# ", end="")
            else:
                print("  ",end="")
        print("|")
    print(config.separator)

def user_input():
    my_list=[]
    print("Enter live cell coordinates as 'row,col' separated by spaces:")
    str_1=input()
    temp_list=str_1.split()
    for i in temp_list:
        pair_list=i.split(",")
        x=int(pair_list[0])-1
        y=int(pair_list[1])-1
        my_list.append((x,y))
    return my_list

def check_coordinates(my_list):
    for i in my_list:
        x=i[0]
        y=i[1]
        if x<0 or x>=config.Rows or y<0 or y>=config.Cols:
            return False
    return True

def tuple_to_grid(grid,tuple_list):
    for x,y in tuple_list:
        grid[x][y]=1

def game_logic(grid):
    new_grid = []
    for i in range(config.Rows):
        row = [0] * config.Cols
        new_grid.append(row)
    for i  in range (config.Rows):
        for j in range(config.Cols):
            counter=count_alive_neighbors(grid,i,j)
            if grid[i][j] == 1:
                if counter == 2 or counter == 3:
                    new_grid[i][j] = 1
            else:
                if counter == 3:
                    new_grid[i][j] = 1
    return new_grid

def count_alive_neighbors(grid,r,c):
    vectors_list=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    counter_res=0
    for x,y in vectors_list:
        new_x=r+x
        new_y=c+y
        if 0 <= new_x < config.Rows and 0 <= new_y < config.Cols:
            if grid[new_x][new_y] == 1:
                counter_res += 1
    return counter_res

def is_over(grid):
    for i in range(config.Rows):
        for j in range(config.Cols):
            if grid[i][j] == 1:
                return False
    return True



