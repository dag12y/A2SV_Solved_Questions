n,k = map(int,input().split())

nums = list(map(int,input().split()))

if k == 1:
    print(nums[-1]-nums[0])
else:
    # find each corresponding difference
    diffs=[]
    for i in range(1,n):
        diffs.append(nums[i] - nums[i-1])
    
    diffs.sort(reverse=True)
    # find total difference
    total=nums[-1] -nums[0]
    #remove the largest k diffs
    ans = total - sum(diffs[:k-1])
    print(ans)


