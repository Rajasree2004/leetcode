'''
784. Letter Case Permutation

Medium

Companies
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
'''
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def recursion(index,array,original):

            if index == len(original):
                if len(array) == 0:
                    return []
                return ["".join(array)]
            

            char = original[index]
            #lower
            lower = recursion(index + 1,array + [char.lower()],original)
            #upper
            if char.isnumeric():
                upper = []
            else:
                upper = recursion(index + 1,array + [char.upper()],original)
            
            return lower + upper
        
        return recursion(0,[],s)