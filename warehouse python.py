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
            lastReachedRightColumn = p-1
            break
        
def GoLeft(arr, i, j, n, lastReachedLeftColumn):
    for p in range(j,-1,-1):
        if arr[i][p] == 1:
            arr[i][p] = -1
        if arr[i][p] == 0:
            lastReachedLeftColumn = p+1
            break
          
def GoDown(arr, i, j, n, lastReachedBottomRow):
    for p in range(i,n):
        if arr[p][j]==1:
            arr[p][j]=-1
        if arr[p][j]==0:
            lastReachedBottomRow=p-1
            break

def GoUp(arr, i, j, n, lastReachedTopRow):
    for p in range(i,-1,-1):
        if arr[p][j]==1:
            arr[p][j]=-1
        if arr[p][j]==0:
            lastReachedTopRow=p+1
            break

n = 5
arr = [[1,1,1,0,1],
       [1,1,1,0,1],
       [0,0,0,0,0],
       [0,1,1,0,1],
       [0,0,0,0,1]]
ways = 0

#find horyzontal ways
for i in range(0,n):
    for j in range (0,n):
        if arr[i][j]!=0:
            break
        helper = j
        if helper == n-1:
            ways += 1
            
#find vertycal ways
for i in range(0,n):
    for j in range (0,n):
        if arr[j][i]!=0: break
        helper = j
        if helper == n-1:
            ways += 1

goods = 0
lastReachedTopRow = 0
lastReachedBottomRow = 0
lastReachedRightColumn = 0
lastReachedLeftColumn = 0

#find the rectangles(goods) in the labyrinth
for i in range(0,n):
    for j in range(0,n):
        if arr[i][j] == 1:
            GoUp(arr, i, j, n, lastReachedTopRow)
            GoDown(arr, i, j, n, lastReachedBottomRow)
            GoRight(arr, i, j, n, lastReachedRightColumn)
            GoLeft(arr, i, j, n, lastReachedLeftColumn)
            ClearElements(arr, lastReachedLeftColumn, lastReachedRightColumn,
                          lastReachedTopRow, lastReachedBottomRow, n)
            goods += 1
        else:
            arr[i][j] = -1

print(ways)
print(goods)

    

