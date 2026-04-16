class Solution:
    def findMin(self, nums: List[int]) -> int:
        # same left and right pointer principles
        # conditionals to double check if going right is actually a larger number or a smaller number

        l, r = 0, len(nums) -1

        res = max(nums)



        while l<r:
            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        
        return nums[l]
        

            
            

