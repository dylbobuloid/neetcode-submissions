class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        countS, countT = {}, {}

        for i in range(len(s)):
            #for the first letter of the s tring
            #if it doesn't exist in the hashmap add it with the value 0  then + 1
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
