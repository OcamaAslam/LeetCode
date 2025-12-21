class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # 'k' is the index where the next unique element goes
        k = 1
        
        # We start iterating from the second element
        for i in range(1, len(nums)):
            # If current element is different from previous
            if nums[i] != nums[i - 1]:
                # Move the unique element to the 'k' position
                nums[k] = nums[i]
                k += 1
                
        return k

# google gemini3 pro solution
#https://gemini.google.com/share/053fdc84bf14