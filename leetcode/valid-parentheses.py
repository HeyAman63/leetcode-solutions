class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # Valid only if the stack is completely empty
        return not stack