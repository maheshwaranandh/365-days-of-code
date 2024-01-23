class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        l=[0,0]
        for i in range(len(nums)):
            if nums[i] in s:
                l[0]=nums[i]
            else:
                s.add(nums[i])
            if (i+1) not in nums:
                l[1]=i+1
        print(s)
        return l
            
