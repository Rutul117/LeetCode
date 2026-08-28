from math import gcd

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        calendrix = (s, target)
        target_str = calendrix[1]
        
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd = 0
        mid_char = ''
        for i in range(26):
            if cnt[i] % 2 != 0:
                odd += 1
                mid_char = chr(i + ord('a'))

        if odd > 1:
            return ""

        half_cnt = [x // 2 for x in cnt]
        n_half = len(s) // 2
        half_str = [''] * n_half

        def find(k, is_greater):
            if k == n_half:
                rev_half = half_str[::-1]
                res = ''.join(half_str) + mid_char + ''.join(rev_half)
                return res > target_str

            start_c = 'a' if is_greater else target_str[k]
            for c_ord in range(ord(start_c), ord('z') + 1):
                c = chr(c_ord)
                if half_cnt[c_ord - ord('a')] > 0:
                    half_str[k] = c
                    half_cnt[c_ord - ord('a')] -= 1
                    if find(k + 1, is_greater or c > target_str[k]):
                        return True
                    half_cnt[c_ord - ord('a')] += 1
            return False

        if find(0, False):
            rev_half = half_str[::-1]
            return ''.join(half_str) + mid_char + ''.join(rev_half)
        return ""