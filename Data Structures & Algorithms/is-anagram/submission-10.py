class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # how do we want to store this value
        # we can to compare each of this letter counts
        # make a map for each word and store the count for every letter as we pass iterate through each letter

        if len(s) != len(t):
            return False

        countS, countT= {}, {}


        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT





            