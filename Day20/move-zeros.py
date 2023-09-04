'''
283. Move Zeroes
Easy
15.1K
380
Companies

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = nums.count(0)
        # for i in range(n):
        #     nums.remove(0)
        # for i in range(n):
        #     nums.append(0)
        i = 0
        for n in nums:
            if n != 0:
                nums[index] = n
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1