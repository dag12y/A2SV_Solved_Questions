n,m = map(int,input().split())
N = list(map(int,input().split()))
M = list(map(int,input().split()))

i=j=0
ans =0

while i<n and j<m:
    if N[i] == M[j]:
        val = N[i]
        
        countN=0
        while i<n and N[i] == val:
            countN+=1
            i+=1
            
        countM=0
        while j<m and M[j] == val:
            countM+=1
            j+=1
        
        ans+= countN*countM
    elif N[i]<M[j]:
        i+=1
    else:
        j+=1
        
        
        

print(ans)
    
