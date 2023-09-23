'''https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1'''
class Solution:
    def printTriangle(self, N):
        # Code here
        n = N
        for i in range(1,N+1):
            r = 1
            for j in range(n):
                print(r, end=" ")
                r+=1
            n-=1
            print()