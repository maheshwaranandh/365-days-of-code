class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        p=0
        mp=0
        mpyr=logs[0][0]
        k=1950
        while k<=2050:
            # for i in range(len(logs)):
            #     for j in range(2):
            #         if k==logs[i][j]:
            #             if j==0:
            #                 p+=1
            #             else:
            #                 p-=1
            for b,d in logs:
                if k==b:
                    p+=1
                if k==d:
                    p-=1
            if p>mp:
                mp=p
                mpyr=k
            k+=1
        return mpyr
