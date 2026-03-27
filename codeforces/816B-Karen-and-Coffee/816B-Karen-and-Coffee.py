import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())

MAX = 200000 + 2
freq = [0] * MAX

# Step 1: difference array
for _ in range(n):
    l, r = map(int, input().split())
    freq[l] += 1
    freq[r + 1] -= 1

# Step 2: prefix sum to get actual counts
for i in range(1, MAX):
    freq[i] += freq[i - 1]

# Step 3: build good array
good = [0] * MAX
for i in range(MAX):
    if freq[i] >= k:
        good[i] = 1

# Step 4: prefix sum on good
pref = [0] * MAX
for i in range(1, MAX):
    pref[i] = pref[i - 1] + good[i]

# Step 5: answer queries
for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])