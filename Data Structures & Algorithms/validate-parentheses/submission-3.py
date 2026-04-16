class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")" : "(" ,"]" : "[" ,"}" : "{"}

        for c in s:
            if c not in bracket:
                stack.append(c)
            else:
                if stack and stack[-1] == bracket[c]:
                    stack.pop()
                else:
                    return False

        return not stack

        
