'''https://practice.geeksforgeeks.org/problems/triangle-number/1?page=1&status[]=solved&sortBy=submissions'''

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            n = 1
            for j in range(i):
                print(n, end=" ")
                n+=1
            print()