class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <=r:
            k = (l+r) // 2
            hours = 0

            for p in piles:
                # Divide how many times k can go into p
                # We round up to to the next whole value with math.ceiling
                hours += math.ceil(p / k)

            ## If th
            if hours <= h:
                res = min(res, k) 
                r = k - 1
            else:
                l = k + 1
        return res