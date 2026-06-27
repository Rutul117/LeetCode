class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        start, max_len = 0, 1

        for i in range(len(s)):
            # Odd-length palindromes
            odd_palindrome = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd_palindrome == odd_palindrome[::-1]:
                start = i - max_len - 1
                max_len += 2

            # Even-length palindromes
            even_palindrome = s[i - max_len:i + 1]
            if i - max_len >= 0 and even_palindrome == even_palindrome[::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]