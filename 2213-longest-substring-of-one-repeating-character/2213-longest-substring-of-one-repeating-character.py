from sortedcontainers import SortedDict
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        arr = list(s)
        n = len(arr)
        k = len(queryIndices)
        result = [0] * k

        segments = SortedDict()   
        counts = SortedDict()     

        def add_len(length):
            if length > 0:
                counts[length] = counts.get(length, 0) + 1

        def remove_len(length):
            if length > 0:
                counts[length] -= 1
                if counts[length] == 0:
                    del counts[length]

       
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] == arr[i]:
                j += 1
            length = j - i
            segments[i] = length
            add_len(length)
            i = j

        for q in range(k):
            idx = queryIndices[q]
            c = queryCharacters[q]

            if arr[idx] == c:
                result[q] = counts.peekitem(-1)[0]
                continue

            pos = segments.bisect_right(idx) - 1
            start = segments.peekitem(pos)[0]
            length = segments.peekitem(pos)[1]
            end = start + length - 1

            del segments[start]
            remove_len(length)

            left_len = idx - start
            right_len = end - idx

            if left_len > 0:
                segments[start] = left_len
                add_len(left_len)
            if right_len > 0:
                segments[idx + 1] = right_len
                add_len(right_len)

            arr[idx] = c

            new_start = idx
            new_len = 1

            if idx > 0:
                left_pos = segments.bisect_right(idx - 1) - 1
                if left_pos >= 0:
                    l_start = segments.peekitem(left_pos)[0]
                    l_len = segments.peekitem(left_pos)[1]
                    if l_start + l_len - 1 == idx - 1 and arr[l_start] == c:
                        new_start = l_start
                        new_len += l_len
                        remove_len(l_len)
                        del segments[l_start]

            if (idx + 1) in segments and arr[idx + 1] == c:
                r_len = segments[idx + 1]
                new_len += r_len
                remove_len(r_len)
                del segments[idx + 1]

            segments[new_start] = new_len
            add_len(new_len)

            result[q] = counts.peekitem(-1)[0]

        return result