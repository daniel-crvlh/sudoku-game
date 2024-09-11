# Geeks for geeks solution

def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num):
    
    return (not used_in_row(arr, row, num) and 
           (not used_in_col(arr, col, num) and 
           (not used_in_box(arr, row - row % 3, 
                           col - col % 3, num))))

def solve_sudoku(arr): 

    l =[0, 0]
    
    # If there is no unassigned 
    # location, we are done    
    if(not find_empty_location(arr, l)):
        return True
    
    # Assigning list values to row and col 
    # that we got from the above Function 
    row = l[0]
    col = l[1]
    
    # consider digits 1 to 9
    for num in range(1, 10):
        
        # if looks promising
        if(check_location_is_safe(arr, 
                          row, col, num)):
            
            # make tentative assignment
            arr[row][col]= num

            # return, if success, 
            # ya ! 
            if(solve_sudoku(arr)):    
                
                return True

            # failure, unmake & try again
            arr[row][col] = 0
            
    # this triggers backtracking        
    return False 

# Driver main function to test above functions
def get_solved(list_numbers):

    # if success print the grid
    if(solve_sudoku(list_numbers)):
        return list_numbers
    else:
        print ("No solution exists")
        return list_numbers
