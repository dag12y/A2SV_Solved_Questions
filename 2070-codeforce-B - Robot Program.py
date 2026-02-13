q=int(input())
for _ in range(q):
    n,x,k = map(int,input().split())
    command = input().strip()
    
    pref=0
    first_hit=-1
    
    #find the first time reaching 0
    for i in range(n):
        if command[i] == 'L':
            pref-=1
        elif command[i] == 'R':
            pref+=1
        if x+pref == 0:
            first_hit = i+1
            break
    if first_hit == -1 or first_hit>k:
        print(0)
        continue
    
    #find cycle lenght assuming x=0
    pref=0
    cycle_len = -1
    
    for i in range(n):
        if command[i] == 'L':
            pref-=1
        else:
            pref+=1
        if pref == 0:
            cycle_len=i+1
            break
        
    if cycle_len == -1:
        print(1)
    else:
        remaining = k-first_hit
        print(1+remaining // cycle_len)
