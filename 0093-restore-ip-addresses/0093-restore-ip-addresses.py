class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, parts, path):
            # If 4 parts are built, ensure we've consumed entire string
            if parts == 4:
                if i == n:
                    res.append(".".join(path))
                return

            # At most 3 digits per segment
            for length in range(1, 4):
                if i + length > n:
                    break

                segment = s[i:i+length]

                # Reject leading-zero inputs unless it's just "0"
                if segment[0] == '0' and length > 1:
                    continue

                # Segment must be <= 255
                if int(segment) > 255:
                    continue

                backtrack(i + length, parts + 1, path + [segment])

        backtrack(0, 0, [])
        return res
