class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while(l<=r):
            print(l,r)
            if arr[l]>arr[l+1]:
                return l
            if arr[r]>arr[r-1]:
                return r
            l+=1
            r-=1
