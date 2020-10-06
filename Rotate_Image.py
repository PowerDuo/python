"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
                 
Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution {
    public void rotate(int[][] matrix) {
        for(int x=0;x < matrix.length/2;x++){
            for(int y=x;y<matrix.length-x-1;y++){
                //int temp=matrix[x][y];
                matrix[x][y]+=matrix[matrix.length-1-y][x];
                matrix[matrix.length-1-y][x]=matrix[x][y]-matrix[matrix.length-1-y][x];
                matrix[x][y]-=matrix[matrix.length-1-y][x];
                
                matrix[matrix.length-1-y][x]+=matrix[matrix.length-1-x][matrix.length-1-y];
                matrix[matrix.length-1-x][matrix.length-1-y]=matrix[matrix.length-1-y][x]-matrix[matrix.length-1-x][matrix.length-1-y];
                matrix[matrix.length-1-y][x]-=matrix[matrix.length-1-x][matrix.length-1-y];
                
                matrix[matrix.length-1-x][matrix.length-1-y]+=matrix[y][matrix.length-1-x];
                matrix[y][matrix.length-1-x]=matrix[matrix.length-1-x][matrix.length-1-y]-matrix[y][matrix.length-1-x];
                matrix[matrix.length-1-x][matrix.length-1-y]-=matrix[y][matrix.length-1-x];
                //matrix[y][matrix.length-1-x]=temp;
            }   
        } 
    }
}
