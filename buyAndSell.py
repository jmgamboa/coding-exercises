# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        for idx, i in enumerate(prices):
            for jdx, j, in enumerate(prices):
                if idx != jdx:
                    if i < j:
                        print('is less than')
                        profit = j - i

                        if profit > max_profit:
                            max_profit = profit
                print(f'curr profit {max_profit}')
        return max_profit

p = [7,1,5,3,6,4]
print(Solution().maxProfit(p))
