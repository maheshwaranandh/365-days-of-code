class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(len(d)):
            names[i]=d[heights[i]]
        return names
