'''
392. Is Subsequence
Easy
8.3K
453
Companies

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

 '''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # l = [i for i in t]
        # m = [i for i in s]
        # d = set(t)
        # if(len(d) == len(s)):
        #     if(s in t):
        #         return True
        #     else:
        #         return False
        # else:
        #     for i in t:
        #         if i not in m:
        #             l.remove(i)
        #         print(l)
        #     l = "".join(l)
        #     if(l == s):
        #         return True
        #     else:
        #         return False
        i,j=0,0
        m=len(s)
        n=len(t)
        while(i<m and j<n):
            if s[i]==t[j]:
                i+=1
                j+=1            
            else:
                j+=1
        if i==len(s):
            return True
        else:
            return False