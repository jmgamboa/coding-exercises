# https://leetcode.com/problems/two-sum/

class Solution:
	def twoSum(self, nums, target):
		copy_nums = nums
		target_list = []
		for idx, i in enumerate(nums):

			if target - nums[idx] in target_list:
				return [nums.index(target - nums[idx]), idx]
			else:
				target_list.append(i)


nums = [3,2,4]
target = 6
nums = [2,7,11,15]
target = 9
print((Solution().twoSum(nums, 9)))