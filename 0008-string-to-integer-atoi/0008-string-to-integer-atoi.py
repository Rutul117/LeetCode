class Solution:
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        sign = 1
        result = 0

        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result