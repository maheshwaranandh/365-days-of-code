class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=[0]*len(mat)
        col=[0]*len(mat[0])
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    c+=1

        return c
