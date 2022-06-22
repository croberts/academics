"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

"""
Plan A: Brute Force - for loop


Plan B: Two pointers


"""


class Solution:
    def twoSum(self, nums, target):
      first_p = 0
      second_p = 1

      while first_p < len(nums):
        while second_p < len(nums):
          #print(first_p, second_p)
          if nums[first_p] + nums[second_p] == target:
            return [first_p, second_p]
          second_p += 1
        first_p += 1
        second_p = first_p + 1

s = Solution()
nums_0 = [2,7,11,15]
target_0 = 9

nums_1 = [3,2,4]
target_1 = 6

print(s.twoSum(nums_0, target_0))
print(s.twoSum(nums_1, target_1))
