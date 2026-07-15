import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=(n)*(1+(n-1))
        sumeven=(n)*(2+(n-1))
        return math.gcd(sumodd,sumeven)