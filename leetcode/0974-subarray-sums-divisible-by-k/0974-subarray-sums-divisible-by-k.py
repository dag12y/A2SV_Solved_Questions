class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        mod_count = {0: 1}  

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod in mod_count:
                count += mod_count[mod]
                mod_count[mod] += 1
            else:
                mod_count[mod] = 1

        return count