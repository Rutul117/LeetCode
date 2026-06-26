class Solution:
    def isValid(self, s: str) -> bool:
        hashmap ={
            ')':'(',
            ']':'[',
            '}':'{'}
        stk = []

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    poppped = stk.pop()
                    if poppped != hashmap[c]:
                        return False
        return not stk