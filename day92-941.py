class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        dir=0
        prev=arr[0]
        for i in range(1,len(arr)):
            if dir==0:
                if prev>arr[i]:
                    if i==1:
                        return False
                    else:
                        dir=1
                elif prev==arr[i]:
                    return False  
            else:
                if prev<arr[i]:
                    return False
                elif prev==arr[i]:
                    return False
            prev=arr[i]
        if dir==0:
            return False
        return True     
