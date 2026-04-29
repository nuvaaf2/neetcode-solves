class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')':'(', '}':'{',']':'['}

        for char in s:
            if char in mapping:
                top = stack[-1] if stack else '#'
                if mapping[char] != top:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return not stack
                    



        