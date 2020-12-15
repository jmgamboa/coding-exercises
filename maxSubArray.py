# https://leetcode.com/problems/maximum-subarray/
# Dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass
        # i = 0
        # j = 1
        # t = len(nums)
        # curr_val = nums[0]
        # curr_nums = [nums[0]]
        # for i in nums:
        #     for jdx, j in enumerate(nums):
        #         if i + j > nums[0]:
        #             curr_vaal = i + j
        #             curr_nums.append()









nums = [-2,1,-3,4,-1,2,1,-5,4]

print(Solution().maxSubArray(nums))