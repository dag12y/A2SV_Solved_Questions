from collections import Counter
t=int(input())

def solve(n,k,s):
    count = Counter(s[:k])
    ans = count['W']
    for i in range(k,n):
        count[s[i-k]]-=1
        count[s[i]]+=1
        ans = min(ans, count['W'])
    return ans

for _ in range(t):
    n,k = map(int,input().split())
    s=input()
    print(solve(n,k,s))