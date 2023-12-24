class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        k=sorted(nums)
        l=0
        r=1
        while(r<len(k)):
            if k[l]==k[r]:
                l+=2
                r+=2                
                continue
            else:
                return False

        return True
