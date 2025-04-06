from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        # Backtrack to find the subset
        result = []
        current = max_index
        while current != -1:
            result.append(nums[current])
            current = prev[current]
        
        return result[::-1]

solution = Solution()
nums = [1, 2, 3]
result = solution.largestDivisibleSubset(nums)
print(result)