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
        x=int(pair_list[0])
        y=int(pair_list[1])
        my_list.append((x,y))
    return my_list

def check_coordinates(my_list):
    for i in my_list:
        x=i[0]
        y=i[1]
        if x<0 or x>=config.Rows or y<0 or y>=config.Cols:
            return False
    return True








