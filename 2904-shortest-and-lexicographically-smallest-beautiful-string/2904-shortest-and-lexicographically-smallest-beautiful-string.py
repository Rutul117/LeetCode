class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1')<k: return ""
        n=len(s)
        minLen, cnt1, Len=n, 0, 0
        xMin, win=1<<n, 0
        l=0
        for r, c in enumerate(s):
            is1=c=='1'
            win=(win<<1)|is1
            cnt1+=is1
            Len+=1
            while cnt1>k or (cnt1==k and s[l]=='0'):
                win&=(1<<(Len-1))-1
                Len-=1
                cnt1-=s[l]=='1'
                l+=1
            if cnt1==k:
                if Len<minLen:
                    minLen, xMin=Len, win
                elif Len==minLen and win<xMin:
                    xMin=win
        return bin(xMin)[2:]