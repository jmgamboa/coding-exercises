# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers, target):
        res = []
        pointer_1 = 0
        pointer_2 = 1

        while pointer_1 < len(numbers):
            curr_val = numbers[pointer_1]

            target_diff = target - curr_val

            if not numbers[pointer_2] == target_diff:
                if pointer_2 == len(numbers)-1:
                    pointer_1 += 1
                    pointer_2 = pointer_1 + 1
                else:
                    pointer_2 += 1
            else:
                return res[pointer_1+1, pointer_2+1]


class Solution:
    def twoSum(self, numbers, target):
        j = 0
        i = len(numbers)-1

        while j < len(numbers):
            total = numbers[j] + numbers[i]
            if total == target:
                return [j+1, i+1]
            elif total < target_diff:
                j += 1
            else:
                i -= 1



n = [5,25,75]
t = 100
print(Solution().twoSum(n, t))
