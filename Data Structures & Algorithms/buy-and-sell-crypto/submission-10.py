class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mostP = 0
        l, r = 0, 1

        while r < len(prices):
            currentProfit = prices[r] - prices[l]

            if prices[r] > prices[l]:
                mostP = max(currentProfit, mostP)
            else: 
                l = r
            r += 1

        return mostP



        
        # Sliding windo
        # keep sliding the window untill l or r reaches the end
        # maxProfit = 0
        # currentProfit = l - r

        # if l < r l = r and r += 1

        
            






        