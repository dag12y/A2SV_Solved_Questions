from collections import Counter

    cnt_t = Counter(t)
    cnt_s = Counter(s)

    # check if possible at all
    ok = True
    for c in cnt_s:
        if cnt_t[c] < cnt_s[c]:
            ok = False
            break

    if not ok:
        print("Impossible")
        continue

    rem_s = cnt_s.copy()
    i = 0
    res = []

    for _ in range(len(t)):
        for k in range(26):
            c = chr(ord('a') + k)

            if cnt_t[c] == 0:
                continue

            cnt_t[c] -= 1

            advance = False
            if i < len(s) and c == s[i]:
                advance = True
                rem_s[c] -= 1

            possible = True
            for ch in rem_s:
                if cnt_t[ch] < rem_s[ch]:
                    possible = False
                    break

            if possible:
                res.append(c)
                if advance:
                    i += 1
                break
            else:
                cnt_t[c] += 1
                if advance:
                    rem_s[c] += 1

    print("".join(res))