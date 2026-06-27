class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        direction = 1  # 1 for down, -1 for up
        row = 0

        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction

        return ''.join(rows)

# Test cases
solution = Solution()
s1, numRows1 = "PAYPALISHIRING", 3
print(solution.convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2, numRows2 = "PAYPALISHIRING", 4
print(solution.convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

s3, numRows3 = "A", 1
print(solution.convert(s3, numRows3))  # Output: "A"
