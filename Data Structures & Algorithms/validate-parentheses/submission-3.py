class Solution:
    def isValid(self, s: str) -> bool:
        valid = "(){}[]"
        if len(s) % 2 != 0:
            return False
        l = 0
        stack = []
        for c in s:
            if c in "}])":
                if not stack:
                    return False
                pair = stack.pop() + c
                if pair != "[]" and pair != "{}" and pair != "()":
                    return False
            else: 
                stack.append(c)
        return stack == []