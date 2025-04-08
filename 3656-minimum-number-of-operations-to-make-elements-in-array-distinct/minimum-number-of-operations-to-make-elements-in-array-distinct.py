class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        for operations in range(0, (n//3) +2):
            start = operations * 3

            if start >= n:
                return operations
            remaining = nums[start:]
            if len(remaining) == len(set(remaining)):
                return operations
        return (n+2) // 3

solution = Solution()
nums = [1,2,3,4,2,3,3,5,7]
result = solution.minimumOperations(nums)
print(result)
        