class Solution:
    def isApproxMatching(self, query, dictionary):
        for word in dictionary:
            misMatch = 0
            for i in range(0, len(query)):
                if query[i] != word[i]:
                    misMatch+=1
                if misMatch > 2:
                    break
            if misMatch <= 2:
                return True
        return False



    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        words = list()
        for query in queries:
            if self.isApproxMatching(query, dictionary):
                words.append(query)

        return words