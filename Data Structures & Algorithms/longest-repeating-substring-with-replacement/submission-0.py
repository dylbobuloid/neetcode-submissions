class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Map to hold count
        count = {} 
        # hold length of the largest repeating character
        res = 0 
        # left pointer (start of the window)
        l = 0 

        #have the right pointer iterate through the entire length of string s
        for r in range(len(s)):
            #for each letter add the count to the map
            count[s[r]] = 1 + count.get(s[r], 0)

            #(r - l + 1) - max(count.values()) gives you the number of replacement letters needed
            # if the number of replacements is too high slide the window down by one
            if (r - l + 1) - max(count.values()) > k:
                #decrement the count for the letter in our current window
                count[s[l]] -= 1
                #Move the left pointer of the window up one
                l += 1


            # storing the max in the window
            res = max(res, r - l + 1)

        return res