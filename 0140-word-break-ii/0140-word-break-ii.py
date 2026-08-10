class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        # Memoization dictionary
        memo = {}

        def backtrack(start):
            # If the result for this start position is already computed, return it
            if start in memo:
                return memo[start]
            
            result = []
            
            # If we have reached the end of the string, return an empty list indicating a valid path
            if start == len(s):
                return [""]
            
            # Try every possible end position for the current substring
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recurse for the remaining part of the string
                    sub_sentences = backtrack(end)
                    for sub_sentence in sub_sentences:
                        # If sub_sentence is empty, it means it's the end of the string
                        if sub_sentence:
                            result.append(word + " " + sub_sentence)
                        else:
                            result.append(word)
            
            # Memoize the result for the current start position
            memo[start] = result
            return result
        
        return backtrack(0)