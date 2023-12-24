class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        s=0
        r,c=len(matrix),len(matrix[0])
        ans=[[0]*(c) for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    ans[i][j]=matrix[i][j]
                    s+=ans[i][j]
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==0:
                    ans[i][j]=0
                else:
                    ans[i][j]=matrix[i][j]+min(ans[i-1][j],ans[i][j-1],ans[i-1][j-1])
                    s+=ans[i][j]

        return s
