class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop the top element if stack is not empty
                if bracket_map[char] != top_element:  # Check if it matches the corresponding opening bracket
                    return False
            else:  # It's an opening bracket
                stack.append(char)

        return not stack  # If stack is empty, all brackets were matched
