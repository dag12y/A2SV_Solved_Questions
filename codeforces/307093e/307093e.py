n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
freq = {}
ans = 0

for right in range(n):
    x = a[right]
    freq[x] = freq.get(x, 0) + 1

    while len(freq) > k:
        y = a[left]
        freq[y] -= 1
        if freq[y] == 0:
            del freq[y]
        left += 1

    ans += (right - left + 1)

print(ans)