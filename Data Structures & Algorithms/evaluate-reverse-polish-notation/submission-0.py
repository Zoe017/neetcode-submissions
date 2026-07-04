class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = "+-*/"
        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "/":
                    res = int(a / b)
                elif i == "*":
                    res = a * b
                stack.append(res)
        return stack[-1]