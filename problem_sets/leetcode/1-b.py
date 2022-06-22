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

PLan C: dict sum

"""

from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
      d = defaultdict()

      for index, value in enumerate(nums):
        d[value] = d[value].append(index)

      print(d)

      i = 0

      while i < target:
        i += 1
        other = target - i

        #print(i, other, target)

        try:
          if d[other] and i != other:
            return [d[i], d[other]]
        except KeyError:
          pass





s = Solution()
nums_0 = [2,7,11,15]
target_0 = 9

nums_1 = [3,2,4]
target_1 = 6

nums_2 = [3,3]
target_2 = 6

#print(s.twoSum(nums_0, target_0))
#print(s.twoSum(nums_1, target_1))
print(s.twoSum(nums_2, target_2))
