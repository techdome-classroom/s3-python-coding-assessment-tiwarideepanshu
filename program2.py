class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0  # To keep track of the previous value
        
        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < prev_value:
                total -= current_value  # Subtract if current value is less than the previous
            else:
                total += current_value  # Add otherwise
            prev_value = current_value  # Update previous value

        return total
