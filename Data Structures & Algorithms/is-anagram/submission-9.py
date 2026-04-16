class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Not the same length then not anagram
        if len(s) != len(t):
            return False

        # Creating dictionary to hold letters for both
        countS, countT = {}, {}

        # Looping through all of the letters in s and t

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for letter, freq in countS.items():
            print(letter)
            if countT.get(letter) != freq:
                return False

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
                
        
        return True

            