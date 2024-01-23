class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s = int(''.join(list(map(str,digits))))+1
        # return list(map(int,str(s)))
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
        
