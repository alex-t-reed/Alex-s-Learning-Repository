"""
Written by Alex Reed Aparicio

LinkedIn: https://linkedin.com/in/alextreed
YouTube: https://www.youtube.com/@alex_t_reed
LeetCode: https://leetcode.com/u/alex-t-reed/
Medium: https://medium.com/@ar.codes
GitHub: https://github.com/alex-t-reed
TikTok: https://tiktok.com/@ar.codes
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers we've already seen and their indices
        num_dict = {}
        
        # Loop through each number in the list with its index
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference_needed = target - num
            
            # Check if we've already seen the number that makes the sum with the current number
            if difference_needed in num_dict:
                # If we have, return the indices of the two numbers that add up to the target
                return [num_dict[difference_needed], i]
            
            # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list (though this shouldn't happen in this problem)
        return []
    

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    solution = Solution() # Create new instance of Solution
    assert solution.twoSum(nums=nums, target=target) == [0,1] # You shouldn't see anything if you run this code as I've tested the function

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

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
