'''
1456. Maximum Number of Vowels in a Substring of Given Length
Medium
3K
99
Companies

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length


'''

class Solution:
    def maxVowels(self, x: str, k: int) -> int:
        # l = []
        # st = 0
        c = 0
        v = "aeiouAEIUO"
        for i in range(k):
            if x[i] in v: c+=1
        m=c
        for i in range(len(x)-k):
            if x[i] in v: c-=1
            if x[i+k] in v: c+=1
            m=max(m,c)
        return m