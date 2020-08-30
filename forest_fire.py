"""
Roco is an island near Africa which is very prone to forest fire. Forst fire is such that is destroys the 
complete forest. Not a  single tree is left. This island has been cursed by God, and the curse is that
whenever a tree catches fire,it passes fire to all its adjacent tree in all 8 directions -
N, S, E, W, NE, NW, SE, SW. And it is given that fire is spreading every minute. Trees (indicated by T)
and water (indicated by W) spots are arranged in a grid of MxN - M rows and N columns.

Input format:
-First line contains two integers, M,N, space separated, giving the size of forest in terms of number of 
    rows and columns respectively 
-The next line contains two integers X,Y, space separated, giving the coordinates of the first tree that 
    catches fire
-The next M lines, where ith line containing N characters each of which is either T or W, giving the 
    position of the tree and Water in the ith row of the foreest.

Output format:
-Single integer indicating the number of minutes taken for the entire forest to catch fire.

Constraints:
3<=M<=20
3<=N<=20

Sample Input - 1

3   3
1   3

W   T   T
T   W   W
W   T   T

Sample Output - 1
5

Explanation: 
In the second minut, tree at (1,2) catches fire. In the third minute, the tree at (2,1) catches fire,
fourth minute tree at (3,2) catches fire and in the fifth minute the last tree at (3,3) catches fire.

Sample Input - 2

6   6  
1   6

W   T   T   T   T   T
T   W   W   W   W   W
W   T   T   T   T   T
W   W   W   W   W   T
T   T   T   T   T   T
T   W   W   W   W   W

Sample Output - 2

16

data_1=[
    ['W', 'T', 'T', 'T', 'T', 'T'], 
    ['T', 'W', 'W', 'W', 'W', 'W'], 
    ['W', 'T', 'T', 'T', 'T', 'T'], 
    ['W', 'W', 'W', 'W', 'W', 'T'], 
    ['T', 'T', 'T', 'T', 'T', 'T'], 
    ['T', 'W', 'W', 'W', 'W', 'W']
]


(1,1,W)   (1,2,T)   (1,3,T)   (1,4,T)   (1,5,T)   (1,6,T)

(2,1,T)   (2,2,W)   (2,3,W)   (2,4,W)   (2,5,W)   (2,6,W)

(3,1,W)   (3,2,T)   (3,3,T)   (3,4,T)   (3,5,T)   (3,6,T)

(4,1,W)   (4,2,W)   (4,3,W)   (4,4,W)   (4,5,W)   (4,6,T)

(5,1,T)   (5,2,T)   (5,3,T)   (5,4,T)   (5,5,T)   (5,6,T)

(6,1,T)   (6,2,W)   (6,3,W)   (6,4,W)   (6,5,W)   (5,6,W)




Step -1:    Input organisation
Input row,col and fire_row, fire_col make 0 Index -- 6,6  1,6  ----> 5,5  0,5


Step -2:
Convert to lists and Get count of total Trees


step - 3    Adjacent elements finding
    Input (fire_row, fire_col)
    returns Array [(int,int)]*8


Step -4
    Validating array returned from step-3
    Logic - M,N > array-elements
    return Array((int,int))

Step -5
    Compare values with T
    If T, replace with F
    store all the F values in an array
    Return(F hue vale elements)


Step -6:
    For loop implementation of returned array from step 5 do step 3


"""

# row1=


# input_line1 = "W T T T T T"
# input_line2 = "T W W W W W"
# input_line3 = "W T T T T T"
# input_line4 = "W W W W W T"
# input_line5 = "T T T T T T"
# input_line6 = "T W W W W W"

# input_fire_tree = "1 6"

# input_lists = [input_line1, input_line2, input_line3, input_line4, input_line5, input_line6]
# input_grid = []

# for input_list in input_lists:    
#     tmp = input_list.replace(" ","")
#     tmp = list(tmp)
#     input_grid.append(tmp)


# list_fire_tree = input_fire_tree.replace(" ","")
# list_fire_tree = list(list_fire_tree)               # Whenever using this, convert it to string


#-----------------Step 3------------------#
def find_adj_element(fire_row, fire_column):
    '''
    Function to find the adjacent elements of fire element
    Argument:
        Tree that is on fire (Row, column)
        fire_row - Integer
        fire_column - Integer
    Returns:
        List of tuples containing the adjacent elements of fire element
    '''

    tuple1 = (fire_row-1,fire_column-1)     
    tuple2 = (fire_row-1,fire_column)
    tuple3 = (fire_row-1,fire_column+1)
    tuple4 = (fire_row,fire_column-1)
    tuple5 = (fire_row,fire_column+1)
    tuple6 = (fire_row+1,fire_column-1)
    tuple7 = (fire_row+1,fire_column)
    tuple8 = (fire_row+1,fire_column+1)

    adj_element_array = [tuple1, tuple2, tuple3, tuple4, tuple5, tuple6, tuple7, tuple8]

    return adj_element_array


#-----------------Step 4------------------#
def validate_element(input_array,row,col):
    '''
    
    Validating if input array falls under the given matrix dimensions
    Argument:
                input_array - input array elements for validation
                row - metrix row dimension value
                col - metrix column dimension value

    Return : valid list of metrix elements
    '''
    valid_elements = []
    for i in input_array:
        if i[0] < 0 or i[0] > row or i[1] < 0 or i[1]> col:
            continue
        else:
            valid_elements.append(i)
    
    return valid_elements



#----------------- UPDATE BURNT TREES (STEP5) ------------------#
def update_burnt_trees(grid_list, coordinate_list, fire_count):
    new_burnt_tree_list=[]
    for coordinates in coordinate_list:
        if grid_list[coordinates[0]][coordinates[1]] == "T":
            grid_list[coordinates[0]][coordinates[1]] = "F"
            fire_count+=1
            new_burnt_tree_list.append(coordinates)
    return new_burnt_tree_list, grid_list, fire_count





#----------------- INPUT ORGANISATION FUNCTION (STEP 1 & 2) ------------------#
def input_organisation(input_grid_list, total_rows, total_columns, fire_row_no, fire_column_no):

    total_tree_count=0
    rows=0
    columns=0
    fire_row=0
    fire_column=0
    burnt_tree_list=[]
    grid_list=[]
    fire_count=0

    for input_line in input_grid_list:
        temp_list=input_line.split(" ")
        grid_list.append(temp_list)

    total_tree_count = 0
    for list1 in grid_list:
        for i in list1:
            if i=="T":
                total_tree_count+=1

    rows=total_rows-1
    columns=total_columns-1
    fire_row=fire_row_no-1
    fire_column=fire_column_no-1
    tuple_fire=(fire_row, fire_column)
    burnt_tree_list.append(tuple_fire)
    grid_list[fire_row][fire_column]="F"
    fire_count+=1

    while fire_count < total_tree_count:

        for coordinates in burnt_tree_list:
            all_adj_coordinates = find_adj_element(coordinates[0], coordinates[1])
            valid_adj_coordinates = validate_element(all_adj_coordinates, rows, columns)
            burnt_tree_list, grid_list1, fire_count = update_burnt_trees(grid_list, valid_adj_coordinates, fire_count)



    # return(grid_list, rows, columns, fire_row, fire_column, burnt_tree_list, fire_count, total_tree_count)



input_grid_list = ["W T T T T T", "T W W W W W", "W T T T T T", "W W W W W T", "T T T T T T", "T W W W W W"]


grid_list, rows, columns, fire_row, fire_column, burnt_tree_list, fire_count, total_tree_count = input_organisation(input_grid_list, 6, 6, 1, 6)


# grid_list, rows, columns, fire_row, fire_column, burnt_tree_list


# print("Aniruddh ka kata ki nai??")
# print("Rows: ", rows)
# print("Column: ", columns)
# print("burn_tree: ", burnt_tree_list)
# print("Grid List", grid_list)

# time=0
# while fire_count!=total_tree_count:

    # time+=1
# all_adj_coordinates = find_adj_element(fire_row, fire_column)

# print("shivaji ka kata ki nai?")
# print("ans: ", all_adj_coordinates)

# valid_adj_coordinates = validate_element(all_adj_coordinates, rows, columns)
# print("Amol ka kata ki nai?")
# print("Amlya ka ans: ", valid_adj_coordinates)

# new_burnt_tree_list, grid_list1, fire_count = update_burnt_trees(grid_list, valid_adj_coordinates, fire_count)
# print(new_burnt_tree_list)

# # print(time)
# print("total_tree_count: ", total_tree_count)


# for i in new_burnt_tree_list:

#     if fire_count == total_tree_count:
#         break

#     print(i)
#     all_adj_coordinates = find_adj_element(i[0], i[1])

#     print("shivaji ka kata ki nai?")
#     print("ans: ", all_adj_coordinates)

#     valid_adj_coordinates = validate_element(all_adj_coordinates, rows, columns)
#     print("Amol ka kata ki nai?")
#     print("Amlya ka ans: ", valid_adj_coordinates)

#     new_burnt_tree_list, grid_list1, fire_count = update_burnt_trees(grid_list, valid_adj_coordinates, fire_count)
#     print(new_burnt_tree_list)

# print(fire_count)


'''
Aniruddh ka kata ki nai??
Rows:  0
Column:  0
burn_tree:  [(1, 6)]
Grid List [['W', 'T', 'T', 'T', 'T', 'T'], ['W', 'T', 'T', 'T', 'T', 'T'], ['W', 'T', 'T', 'T', 'T', 'T'], ['W', 'T', 'T', 'T', 'T', 'T'], ['W', 'T', 'T', 'T', 'T', 'T'], ['W', 'T', 'T', 'T', 'T', 'T']]
shivaji ka kata ki nai?
ans:  [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
Amol ka kata ki nai?
Amlya ka ans:  []
'''
