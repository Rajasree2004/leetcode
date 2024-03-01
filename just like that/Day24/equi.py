'''
https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
'''
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        tot = sum(A)
        
        left = 0
        
        for i in range(N):
            right = tot - left - A[i]
            
            if left == right :
                return i+1
                
            left += A[i]
        return -1