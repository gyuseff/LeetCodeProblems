# Link: https://leetcode.com/problems/two-sum
# Status: Solution accepted and beats 87.26%

# Problem statement: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# We can assume there is always an answer

# My solution to this problem is use a hash table together with a for loop
# Create a hash_table with <key, value> as <num, index>; if a number is repeated, the value will be the last index
# Loop over the indexes in the input list, then if target - nums[i] is in the hash_table and it is different to i, then return [i, hash_table[target - num[i]]]
# If both values are the same, then the for loop will catch the first index and the hash_table will have the second index:
# Example, if nums = [3,3] and target = 6 -> index_dict = {3 : 1} -> it will return i = 0 and hash_table[3] = 1

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        index_dict : dict[int,int] = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            n : int = target - nums[i]

            if n in index_dict and index_dict[n] != i:
                return [i, index_dict[n]]
            

    def _twoSum(self, nums, target):
        """
        Old solution for Python (not 3)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """        
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
        # A + B = target
        """
        for i in range(len(nums)):
            B = target - nums[i]
            if B in nums[i+1:]:
                j = nums.index(B,i+1)
                return [i,j]
        """
        
        table = {}
        
        for i in range(len(nums)):
            table[nums[i]] = i
        
        for i in range(len(nums)):
            if(target - nums[i] in table and table[target - nums[i]] != i):
                return [i, table[target - nums[i]]]
