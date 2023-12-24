class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zerorow=[0]*len(grid)
        zerocol=[0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    zerorow[i]+=1
                    zerocol[j]+=1
        
        diff=[[0]*len(grid[0])for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j]=(len(grid)-zerorow[i])+(len(grid[0])-zerocol[j])-(zerorow[i])-(zerocol[j])
        return diff
