'''
345. Reverse Vowels of a String
Easy
3.8K
2.6K
Companies

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']
        l = []
        for i in s:
            if i in v:
                l.append(i)
        l = l[::-1]
        print(l)
        s = [i for i in s]
        j = 0
        for i in range(len(s)):
            if(s[i] in v):
                s[i] = l[j]
                j+=1
        return "".join(s)
