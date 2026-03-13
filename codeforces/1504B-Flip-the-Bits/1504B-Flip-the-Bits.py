t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))

    pref = [0]*n
    zero = one = 0

    for i in range(n):
        if a[i] == 0:
            zero += 1
        else:
            one += 1
        if zero == one:
            pref[i] = 1

    flip = 0
    ok = True

    for i in range(n-1, -1, -1):
        cur = a[i]
        if flip:
            cur ^= 1

        if cur == b[i]:
            continue

        if pref[i]:
            flip ^= 1
        else:
            ok = False
            break

    print("YES" if ok else "NO")