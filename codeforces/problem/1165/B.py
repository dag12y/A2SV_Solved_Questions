n=int(input())
contests = list(map(int,input().split()))

temp = sorted(contests)
day=1
ans=0
for num in temp:
    if num>=day:
        day+=1
        ans+=1
    
print(ans)


codeforces/problem/1165/B
