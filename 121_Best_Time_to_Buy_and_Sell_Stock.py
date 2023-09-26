"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
:type prices: List[int]
:rtype: int
"""

# Solution 1
# While iterating list, extract min price and max profit based on current index
# Time Complexity: O(n) / 765ms(62.62%)
# Memory Complexity: O(1) / 22.46MB(67.70%)
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0] # We also can use sys.maxsize
        max_benefit = 0
        
        for price in prices:
            min_price = min(price, min_price)
            max_benefit = max(max_benefit, price-min_price)
        
        return max_benefit

# Solution 2
# Use two pointers
# Time Complexity: O(n) / 771ms(56.19%)
# Memory Complexity: O(1) / 22.51MB(36.63%)
class Solution(object):
    def maxProfit(self, prices):
        l = 0  # Buy
        r = 1  # Sell
        max_profit = 0
        
        # fix left pointer, move right pointer by one, search max profit
        while r < len(prices):
            buy_price = prices[l]
            sell_price = prices[r]

            # if buy price is lower than sell price, compare profit with max profit
            if buy_price < sell_price:
                current_profit = sell_price - buy_price
                max_profit = max(max_profit, current_profit)
            # if buy price is higher(or same) than sell price, move buy point(l) to sell point(r)
            else:
                l = r

            r += 1

        return max_profit

# Solution 3
# Create gap list, then search the biggest gap
# Time complexity: O(n) / 798ms(20.31%)
# Memory complexity: O(n) / 23.3MB(7.24%)
class Solution(object):
    def maxProfit(self, prices):
        gaps = []
        for i in range(len(prices)-1):
            gaps.append(prices[i+1]-prices[i])
        max_gap = 0
        compare = 0
        for i in range(len(gaps)):
            gap = gaps[i]
            compare += gap
            if compare > max_gap:
                max_gap = compare
            elif compare <= 0:
                compare = 0
        return max_gap 

# Solution 4
# Brute Force with max function
# Time Limit Exceeded(200/212)
class Solution(object):
    def maxProfit(self, prices):
        max_benefit = 0
        for i in range(len(prices)-1):
            benefit = max(prices[i+1:]) - prices[i]
            if benefit > max_benefit:
                max_benefit = benefit
        return max_benefit

# Solution 5
# Brute Force
# Time Limit Exceeded(199/212)
class Solution(object):
    def maxProfit(self, prices):
        # find out max_benefit
        max_benefit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for sell_price in (prices[i+1:]):
                benefit = sell_price - buy_price
                if benefit > max_benefit:
                    max_benefit = benefit
        return max_benefit