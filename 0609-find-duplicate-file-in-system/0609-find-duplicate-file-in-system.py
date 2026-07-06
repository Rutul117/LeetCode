class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for s in paths:             
            s = s.split(' ')                
            path = s.pop(0)                 

            for file in s:
                idx = file.index('(')       
                d[file[idx:]].append(path+'/'+file[:idx]) 

        return [d[i] for i in d.keys() if len(d[i]) > 1]