class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the shortest string (prefix can't be longer than this)
        prefix = min(strs, key=len)
        
        for i in range(len(prefix)):
            for s in strs:
                if s[i] != prefix[i]:
                    return prefix[:i]
        
        return prefix