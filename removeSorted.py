# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution:
	def removeDuplicates(self, nums) -> int:
		if len(nums) in [0, 1]:
			return len(nums)
		t = len(nums) - 1
		i, j = 0, 1
		while (t):
			if nums[i] == nums[j]:
				nums.pop(i)
			else:
				i += 1
				j += 1
			t -= 1
		return len(nums)


nums = [1,1,2]

print(Solution().removeDuplicates(nums))
