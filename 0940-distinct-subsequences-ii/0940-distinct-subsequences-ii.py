class Solution:
    def distinctSubseqII(self, s: str) -> int:
    
        n=len(s)
        dp=[0]*(n)
        dp[0]=2
        mp=defaultdict(int)
        mp[s[0]]=0
        for i in range(1,n):
            dp[i]=2*dp[i-1]
            if s[i] in mp:
                dp[i]-=(dp[mp[s[i]]-1] if mp[s[i]]>0 else 1)
            mp[s[i]]=i
            dp[i]%=(10**9+7)
        return (dp[-1]-1+10**9+7)%(10**9+7)