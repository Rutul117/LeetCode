class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        n = len(cleaned)

        for i in range(n // 2):
            if cleaned[i] != cleaned[n - 1 - i]:
                return False

        return True