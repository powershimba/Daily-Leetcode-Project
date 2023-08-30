"""
1672. Richest Customer Wealth 

You are given an m x n integer grid accounts where accounts[i][j] 
is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
"""


"My Solution"

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """ 
        
        max_wealth = 0
        for i in range(len(accounts)):
            sum_of_wealth = 0
            for j in range(len(accounts[i])):
                sum_of_wealth += accounts[i][j]
            if sum_of_wealth > max_wealth:
                max_wealth = sum_of_wealth
        return max_wealth

"""
More Simple Solution

class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(acc) for acc in accounts)
"""