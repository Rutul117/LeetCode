class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to map roman numerals to their integer values
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the result
        result = 0
        
        # Iterate over the string from right to left
        for i in range(len(s) - 1, -1, -1):
            # If the current numeral is smaller than the next one, subtract its value
            if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                result -= roman_numerals[s[i]]
            # Otherwise, add its value to the result
            else:
                result += roman_numerals[s[i]]
        
        return result