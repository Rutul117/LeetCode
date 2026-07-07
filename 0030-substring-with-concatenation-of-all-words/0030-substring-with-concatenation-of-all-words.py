from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            substr = s[i:i + total_length]
            substr_count = Counter([substr[j:j + word_length] for j in range(0, total_length, word_length)])
            if substr_count == word_count:
                result.append(i)

        return result
