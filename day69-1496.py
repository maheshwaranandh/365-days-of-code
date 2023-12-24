class Solution:
    def isPathCrossing(self, path: str) -> bool:
        l=[0,0]
        k=[(0,0)]
        for i in path:
            if i=="N":
                l[1]+=1
            elif i=="S":
                l[1]-=1
            elif i=="W":
                l[0]-=1
            else:
                l[0]+=1
            
            if tuple(l) in k:
                return True
            k.append(tuple(l))
        return False


            
        
