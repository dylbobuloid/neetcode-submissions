class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []

        for n in tokens:
            if n == '+':
                secondVal = stack.pop()
                firstVal = stack.pop()

                result = (firstVal + secondVal)
                stack.append(result)

            elif n == '-':
                secondVal = stack.pop()
                firstVal = stack.pop()

                result = (firstVal - secondVal)
                stack.append(result)

            elif n == '/':
                secondVal = stack.pop()
                firstVal = stack.pop()

                result = int(firstVal / secondVal)
                stack.append(result)

            elif n == '*':
                secondVal = stack.pop()
                firstVal = stack.pop()

                result = (firstVal * secondVal)
                stack.append(result)


            else:
                stack.append(int(n))

        return stack.pop()

        