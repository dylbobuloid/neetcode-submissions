class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        

        for r in range(len(s)):
            while s[r] in charSet:##if the character is in the charSet
                charSet.remove(s[l])#remove the leftmost character from the set to make the string contiguous
                l += 1 #shuffle he left pointer down one
            charSet.add(s[r])# adds a character that is not yet in the charSet, either we removed it or it is a new character
            res = max(res, r - l + 1)# makes the res larger if the current window size is larger
        return res
