class Solution {
    public int projectionArea(int[][] grid) {
        int a=0,b=0,c=0,max=0,max1=0;
        for(int i=0;i<grid.length;i++){
            max=0;max1=0;
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]!=0){
                    a++;
                }
                max=Math.max(max,grid[i][j]);
                max1=Math.max(max1,grid[j][i]);
            }
            b+=max;
            c+=max1;
        }
        return a+b+c;


    }
}
