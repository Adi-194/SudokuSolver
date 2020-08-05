def printsudoku(arr):
    for i in range(9):
        temp =  str(arr[i])
        print("".join(temp))

def checkrow(arr,row,num):
    for i in range(9):
        if arr[row][i]==num:
            return True
    return False

def checkcol(arr,col,num):
    for i in range(9):
        if arr[i][col]==num:
            return True
    return False

def checkbox(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col]==num:
                return True
    return False

def checkempty(arr,l):
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                l[0]=i
                l[1]=j
                return True
    return False

def iflocsafe(arr,row,col,num):
    return not checkrow(arr,row,num) and not checkcol(arr,col,num) and not checkbox(arr,row - row % 3,col - col % 3, num)

def solve(arr):
    
    l=[0,0]

    if(not checkempty(arr,l)):
        return True

    row = l[0] 
    col = l[1]

    for num in range(1,10):
        if(iflocsafe(arr,row,col,num)):
            arr[row][col]=num
            if(solve(arr)):
                return True
            arr[row][col]=0
    
    return False

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid =[[0 for x in range(9)]for y in range(9)] 
      
    # assigning values to the grid 
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 
      
    # if success print the grid 
    if(solve(grid)): 
        printsudoku(grid) 
    else: 
        print("No solution exists")
