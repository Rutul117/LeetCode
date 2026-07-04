class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the Roman numeral symbols and their corresponding values
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        # Initialize the result string
        result = ''
        
        # Iterate through the Roman numeral symbols in reverse order
        for value in sorted(roman_numerals.keys(), reverse=True):
            # Repeat the current Roman numeral symbol as many times as possible
            while num >= value:
                # Subtract the value from the integer and append the corresponding Roman numeral to the result
                num -= value
                result += roman_numerals[value]
        
        return result
