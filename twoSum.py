# https://leetcode.com/problems/two-sum/

class Solution:
	def twoSum(self, nums, target):
		copy_nums = nums
		target_dict = {}
		for idx, i in enumerate(nums):

			if target - nums[idx] in target_dict.values():
				return [target-nums[idx], i]
			else:
				target_dict[idx] = i
			print(f'{target - nums[idx]}')
			print(f'target dict {target_dict}')


nums = [3,2,4]
target = 6
nums = [2,7,11,15]
target = 9
(Solution().twoSum(nums, 9))