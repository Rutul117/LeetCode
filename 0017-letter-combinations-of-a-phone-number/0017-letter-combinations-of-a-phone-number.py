class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(index, path):
            # If the current combination is done
            if index == len(digits):
                combinations.append(''.join(path))
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            # Loop through the letters
            for letter in possible_letters:
                # Add the letter to the current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations