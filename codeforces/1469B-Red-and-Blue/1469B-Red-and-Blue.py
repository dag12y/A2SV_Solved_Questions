t=int(input())

def solve(n,r,m,b):
    current_sum=0
    for i in range(1,n):
        r[i]+=r[i-1]
    for j in range(1,m):
        b[j]+=b[j-1]
    ans = max(r)+max(b)
    return max(0,ans,max(r),max(b))

for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    print(solve(n,r,m,b))