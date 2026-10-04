class Solution(object):
    '''def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result'''
    def two_sum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

