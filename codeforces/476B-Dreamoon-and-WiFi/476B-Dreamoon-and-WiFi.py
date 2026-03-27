def backtrack(i, total):
    global valid
    
    if i == k:
        if current + total == target:
            valid += 1
        return
    
    backtrack(i + 1, total + 1)   # '+'
    backtrack(i + 1, total - 1)   # '-'

backtrack(0, 0)

if k == 0:
    print(1 if current == target else 0)
else:
    print(valid / (2 ** k))