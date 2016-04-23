def ClearElements(arr, lastReachedLeftColumn, lastReachedRightColumn,
                  lastReachedTopRow, lastReachedBottomRow, n):
    for i in range(lastReachedLeftColumn,lastReachedRightColumn+1):
        for j in range(lastReachedTopRow,lastReachedBottomRow+1):
             arr[j][i] = -1
            
def GoRight(arr, i, j, n, lastReachedRightColumn):
    for p in range(j,n):
        if arr[i][p] == 1:
            arr[i][p] = -1
        if arr[i][p] == 0:
            lastReachedRightColumn[0] = p-1
            break
        elif (p == n - 1):
            lastReachedRightColumn[0] = p
        
def GoLeft(arr, i, j, n, lastReachedLeftColumn):
    for p in range(j,-1,-1):
        if arr[i][p] == 1:
            arr[i][p] = -1
        if arr[i][p] == 0:
            lastReachedLeftColumn[0] = p+1
            break
        elif (p == 0):
            lastReachedLeftColumn[0] = p
          
def GoDown(arr, i, j, n, lastReachedBottomRow):
    for p in range(i,n):
        if arr[p][j]==1:
            arr[p][j]=-1
        if arr[p][j]==0:
            lastReachedBottomRow[0] = p-1
            break
        elif (p == n - 1):
            lastReachedBottomRow[0] = p

def GoUp(arr, i, j, n, lastReachedTopRow):
    for p in range(i,-1,-1):
        if arr[p][j]==1:
            arr[p][j]=-1
        if arr[p][j]==0:
            lastReachedTopRow[0] = p+1
            break
        elif (p == 0):
            lastReachedTopRow[0] = p

n = 3
arr = [[1,1,1],
       [1,1,1],
       [0,0,0]]

goods = 0
lastReachedTopRow = [0]
lastReachedBottomRow = [0]
lastReachedRightColumn = [0]
lastReachedLeftColumn = [0]

#find the rectangles(goods) in the labyrinth
for i in range(0,n):
    for j in range(0,n):
        if arr[i][j] == 1:
            GoUp(arr, i, j, n, lastReachedTopRow)
            GoDown(arr, i, j, n, lastReachedBottomRow)
            GoRight(arr, i, j, n, lastReachedRightColumn)
            GoLeft(arr, i, j, n, lastReachedLeftColumn)
            ClearElements(arr, lastReachedLeftColumn[0],
                          lastReachedRightColumn[0], 
                          lastReachedTopRow[0], lastReachedBottomRow[0], n)
            goods += 1
        else:
            arr[i][j] = -1

print(goods)

    

