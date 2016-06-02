def MakeNeighborsBadStrawberries(arr, arri, arrj, day, indexi, indexj):
    if(indexi-1 != -1 and arr[indexi-1][indexj] != 1 and
       arr[indexi-1][indexj] != day-1):
        arr[indexi - 1][indexj] = day
    if(indexj-1 != -1 and arr[indexi][indexj-1] != 1 and
       arr[indexi][indexj - 1] != day-1):
        arr[indexi][indexj - 1] = day
    if(indexj + 1 != arrj and arr[indexi][indexj + 1] != 1 and
       arr[indexi][indexj + 1] != day-1):
        arr[indexi][indexj + 1] = day
    if(indexi+1 != arri and arr[indexi+1][indexj] != 1 and
       arr[indexi+1][indexj] != day-1):
        arr[indexi + 1][indexj] = day
        
K = 8
L = 10

i1 = 1
j1 = 6
i2 = 3
j2 = 7


arr = [[0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,1 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,1 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
       [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0]]

day = 2
MakeNeighborsBadStrawberries(arr, K, L, day, i1, j1)
MakeNeighborsBadStrawberries(arr, K, L, day, i2, j2)
day = day + 1
MakeNeighborsBadStrawberries(arr, K, L, day, i1 - 1, j1)
MakeNeighborsBadStrawberries(arr, K, L, day, i1, j1 - 1)
MakeNeighborsBadStrawberries(arr, K, L, day, i1, j1 + 1)
MakeNeighborsBadStrawberries(arr, K, L, day, i1 + 1, j1)
MakeNeighborsBadStrawberries(arr, K, L, day, i2 - 1, j2)
MakeNeighborsBadStrawberries(arr, K, L, day, i2, j2 - 1)
MakeNeighborsBadStrawberries(arr, K, L, day, i2, j2 + 1)
MakeNeighborsBadStrawberries(arr, K, L, day, i2 + 1, j2)

for p in range(8):
    for q in range(10):
        print arr[p][q],
    print "\n"
        






