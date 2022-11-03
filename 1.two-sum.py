#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #dict is better for choosing index.
        
        # create an empty dict
        num = {}

        #utilize for loop to get the index
        for i in range(len(nums)):
            
            if num.__contains__(target-nums[i]):
                return [num.get(target-nums[i]), i]
            else:
                num[nums[i]] = i 
            
        
# @lc code=end

