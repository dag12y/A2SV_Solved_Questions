class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        i,j=0,1
        lengthofArr=len(arr)
        while j<lengthofArr:
            if arr[i]>arr[j]:
                return False
            i=j
            j+=1
        return True