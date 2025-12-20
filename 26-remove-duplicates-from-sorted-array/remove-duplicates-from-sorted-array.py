class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 0
        prev = None
        for i in nums:
            if i != prev:
                nums[k] = i
                prev = i
                k += 1
        
        return k        

        