class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        prev=nums[0]
        m=0
        f=0
        c=0
        for i in range(1,len(nums)):
            if nums[i]==prev:
                c+=1
                
            else:
                c=0
            if c==2:
                print(nums[i])
                f=1
                m=max(m,int(nums[i]))
                c=0

            prev=nums[i]
            
        return str(m)*3 if f==1 else ""
