class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        list1Map = {}
        for i in range(len(list1)):
            list1Map[list1[i]] = i
        ans = []
        indexCount = float('inf')
        for i in range(len(list2)):
            if list2[i] in list1Map:
                list1Index = list1Map[list2[i]]
                minIndexCOunt = list1Index + i
                if indexCount > minIndexCOunt:
                    indexCount = minIndexCOunt
                    ans = [list2[i]]
                elif minIndexCOunt == indexCount:
                    ans.append(list2[i])
        return ans