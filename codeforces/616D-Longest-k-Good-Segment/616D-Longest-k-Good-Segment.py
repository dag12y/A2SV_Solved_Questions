from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
l = 0

best_len = 0
best_l = 0

for r in range(n):
    count[a[r]] += 1
    
    while len(count) > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            del count[a[l]]
        l += 1
    
    if r - l + 1 > best_len:
        best_len = r - l + 1
        best_l = l

print(best_l + 1, best_l + best_len)