class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the words into a single string separated by a single space
        return ' '.join(words)

# Test cases
solution = Solution()
print(solution.reverseWords("the sky is blue"))       # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))      # Output: "world hello"
print(solution.reverseWords("a good   example"))     # Output: "example good a"
