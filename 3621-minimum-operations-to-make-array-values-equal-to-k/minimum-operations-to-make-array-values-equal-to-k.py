from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Check if any number is less than k
        if any(num < k for num in nums):
            return -1
        
        # If all numbers are already k
        if all(num == k for num in nums):
            return 0
        
        # Collect all unique numbers greater than k
        unique_nums = sorted(set(num for num in nums if num > k), reverse=True)
        
        operations = 0
        current_target = k
        
        # We need to reduce each unique number down to k
        # Each step, we can reduce all instances of the largest remaining number to the next lower number or directly to k
        for num in unique_nums:
            operations += 1
        
        return operations

solution = Solution()
nums = [2,1,2]
k = 2
result = solution.minOperations(nums, k)
print(result)