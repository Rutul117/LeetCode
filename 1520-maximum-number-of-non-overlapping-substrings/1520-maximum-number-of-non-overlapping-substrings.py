class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        locs = {}
        for i, x in enumerate(s): 
            locs.setdefault(x, []).append(i)
        
        def fn(lo, hi): 
            """Return expanded range covering all chars in s[lo:hi+1]."""
            for xx in locs: 
                k0 = bisect_left(locs[xx], lo)
                k1 = bisect_left(locs[xx], hi)
                if k0 < k1 and (locs[xx][0] < lo or hi < locs[xx][-1]): 
                    lo = min(lo, locs[xx][0])
                    hi = max(hi, locs[xx][-1])
                    lo, hi = fn(lo, hi)
            return lo, hi
        
        group = set()
        for x in locs: 
            group.add(fn(locs[x][0], locs[x][-1]))
        
        ans = [] # ISMP (interval scheduling maximization problem)
        prev = -1 
        for lo, hi in sorted(group, key=lambda x: x[1]): 
            if prev < lo: 
                ans.append(s[lo:hi+1])
                prev = hi 
        return ans 