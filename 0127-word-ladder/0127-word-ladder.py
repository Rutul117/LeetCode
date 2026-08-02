class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Check if endWord is not in wordList
        if endWord not in wordList:
            #return 0 as its impossible
            return 0

        #Initialize a hashmap nei to store neighbouring words using defaultdict(list)
        nei = defaultdict(list)
        #Append beginWWord to wordList
        wordList.append(beginWord)
        
        #Iterate in wordList for word
        for word in wordList:
            #Iterate in range(len(word)) for j
            for j in range(len(word)):
                #Initialize pattern to word[:j] + "*" + word[j + 1 :]
                pattern = word[:j] + "*" + word[j + 1 :]
                #Append word to nei[pattern]
                nei[pattern].append(word)

        #Initialize a visit set taking in [beginWord]
        visit = set([beginWord])
        #Initialize a deque q taking in [beginWord]
        q = deque([beginWord])
        #Initialize res to 1
        res = 1

        #Iterate wile q
        while q:
            #Iterate in range(len(q)) for i
            for i in range(len(q)):
                #Initialize word to q.popleft()
                word = q.popleft()
                #Check if word == endWord
                if word == endWord:
                    #return res
                    return res
                
                #Iterate in range(len(word)) for j
                for j in range(len(word)):
                    #Initialize pattern to word[:j] + "*" + word[j + 1 :]
                    pattern = word[:j] + "*" + word[j + 1 :]
                    #Iterate in nei[pattern] for neiWord
                    for neiWord in nei[pattern]:
                        #Check if neiWord not in visit set
                        if neiWord not in visit:
                            #Add neiWord to visit
                            visit.add(neiWord)
                            #Append neiWord to q
                            q.append(neiWord)

            #Update res to +1
            res += 1
            
        #return 0
        return 0

        