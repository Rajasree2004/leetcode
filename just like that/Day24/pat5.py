'''https://practice.geeksforgeeks.org/problems/triangle-pattern/1'''

class Solution:
    def printTriangle(self, N):
        # Code here
        n=N
        for i in range(1, N+1):
            for j in range(n):
                print("*", end=" ")
            n-=1
            print()