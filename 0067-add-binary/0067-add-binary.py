class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range( max(len(a),len(b)) ):
            digitA = ord(a[i]) - ord("0") if len(a) > i else 0
            digitB = ord(b[i]) - ord("0") if len(b) > i else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            carry = total // 2
            res = char + res

        if carry:
            res = "1" + res
        return res
        
    
    def addBinary1(self, a: str, b: str) -> str:
        res = ""
        r = 0
        print(max(len(a), len(b)))
        for i in range(max(len(a), len(b))):
            print(f"Ciclo n.{i}")
            if len(a)-1 < i:
                ca = "0"
            else:
                ca = a[-1-i]
            if len(b)-1 < i:
                cb = "0"
            else:
                cb = b[-1-i]
            if len(a)-1 < i:
                ca = "0"
            if len(b)-1 < i:
                cb = "0"
            print(f"{ca}, {cb}")
            if (ca == "0" and cb == "1") or (ca == "1" and cb == "0"):
                if r == 0:
                    res += "1"
                else:
                    r = 1
                    res += "0"

            elif ca == "0" and cb == "0":
                if r == 0:
                    res += "0"
                else:
                    r = 0
                    res += "1"

            else:
                if r == 0:
                    res += "0"
                    r = 1
                else:
                    res += "1"

        if r == 1:
            res += "1"
        return res[::-1]