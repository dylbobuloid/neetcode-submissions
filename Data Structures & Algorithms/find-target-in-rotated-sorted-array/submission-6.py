class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Create a pointer for l and r

        l, r = 0, len(nums) - 1


        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            
            ## if the mid point is in the lefthand portion

            elif nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1