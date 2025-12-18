class Solution(object):
    def twoSum(self, nums, target):
        compl = {}
        for i, x in enumerate (nums):
            diff = target - x
            if diff in compl:
                return [compl[diff], i]
            else:
                compl[x] = i     

        