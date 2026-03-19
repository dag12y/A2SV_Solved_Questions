t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    ans = 0
    
    for k in range(2, n):
        if k == n - 1:
            outside_max = a[n - 2]
        else:
            outside_max = a[n - 1]
        
        T = max(outside_max, 2 * a[k])
        
        i, j = 0, k - 1
        while i < j:
            if a[i] + a[j] + a[k] > T:
                ans += (j - i)
                j -= 1
            else:
                i += 1
    
    print(ans)