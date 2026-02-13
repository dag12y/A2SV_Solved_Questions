matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
    
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            print(abs(r-2)+abs(c-2))
