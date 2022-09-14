class Solution:
    
    def down(self,mat,i,j,m,n):
        temp_arr = []
        for row in range(i,m):
            temp_arr.append(mat[row][n-1])
        return temp_arr,i,j,m,n-1,'left'
        
    def up(self,mat,i,j,m,n):
        temp_arr = []
        for row in range(m-1,i-1,-1):
            temp_arr.append(mat[row][j])
        return temp_arr,i,j+1,m,n,'right'
    
    def right(self,mat,i,j,m,n):
        temp_arr = []
        for col in range(j,n):
            temp_arr.append(mat[i][col])
        return temp_arr,i+1,j,m,n,'down'
    
    def left(self,mat,i,j,m,n):
        temp_arr = []
        for col in range(n-1,j-1,-1):
            temp_arr.append(mat[m-1][col])
        return temp_arr,i,j,m-1,n,'up'
    
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n= len(matrix),len(matrix[0])
        i,j=0,0
        dirn = 'right'
        while(i<m and j<n):
            if dirn == 'right':
                temp_arr,i,j,m,n,dirn = self.right(matrix,i,j,m,n)
            elif dirn == 'left':
                temp_arr,i,j,m,n,dirn = self.left(matrix,i,j,m,n)
            elif dirn == 'up':
                temp_arr,i,j,m,n,dirn = self.up(matrix,i,j,m,n)
            elif dirn == 'down':
                temp_arr,i,j,m,n,dirn = self.down(matrix,i,j,m,n)
            
            ans += temp_arr
        
        return ans