"""
Author : Robbin Singh
Simple Implementaion of BFS (Breadth First Search)using queue
"""
#Entre Adjancey Matrix of the graph
print("Enter Adjancey matrix")
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries row wise:")
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
print("Adjancey Matrix:")
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()


print("\nDFS :")
visited = [0]*R

queue= [0]

visited[0]=1 #Node Starts From Vertex 0
n = queue.pop(0)
print( n ,end="")
while 1:
    for x in range(0,len(visited)):
        if matrix[n][x] == 1 and visited[x]==0:
            visited[x]=1
            queue.append(x)

    if len(queue)==0:
        break
    else:
        n = queue.pop(0)
        print("->",n,end=" ")





