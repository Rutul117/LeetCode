class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing and leading whitespaces
        s = s.strip()
        
        # Initialize length counter
        length = 0
        
        # Iterate through the string from right to left
        for i in range(len(s) - 1, -1, -1):
            # Check if the current character is a non-space character
            if s[i] != ' ':
                # Increment the length counter
                length += 1
            # Break the loop when encountering a space or reaching the beginning of the string
            elif length > 0:
                break
        
        return length