# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val) -> int:
        strt = 0
        end = len(nums)-1
        while strt <= end:
            if nums[strt] != val:
                strt += 1
            else:
                nums[strt], nums[end] = nums[end], nums[strt]
                end -= 1
        return strt



nums = [3,2,2,3]

# 3 2 3 3


val = 3
# expected is 2

print(Solution().removeElement(nums, val))