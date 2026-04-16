class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for s in strs:
            newStr += str(len(s)) + "#" + s
        return newStr

    def decode(self, s: str) -> List[str]:
        i = 0

        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = 1 + j + length

        return res


