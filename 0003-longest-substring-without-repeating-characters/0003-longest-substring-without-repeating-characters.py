class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 # tracks maximum sibstring
        l = 0 # start of Sliding window
        counter : dict[str, int] = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest