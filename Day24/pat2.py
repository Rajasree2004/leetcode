"""https://practice.geeksforgeeks.org/problems/right-triangle/1?page=1&status[]=solved&sortBy=submissions"""
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(i):
                print("*", end=" ")
            print()
