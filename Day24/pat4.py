'''https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1'''

class Solution:
    def printTriangle(self, N):
        # Code here
        n = 1
        for i in range(1,N+1):
            for j in range(i):
                print(n, end=" ")
            n+=1
            print()