def solve(n,p):
    if n == 2:
        return n, *p
    
    ans = [p[0]]
    
    for i in range(1, n - 1):
        if (p[i] - p[i - 1]) * (p[i + 1] - p[i]) < 0:
            ans.append(p[i])
    
    ans.append(p[-1])
    return len(ans),"\n",*ans




for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    result = solve(n,p)
    print(*result)