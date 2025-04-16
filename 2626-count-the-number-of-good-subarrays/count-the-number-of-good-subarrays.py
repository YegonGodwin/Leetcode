from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        freq = defaultdict(int)
        total_pairs = 0
        res = 0
        
        for right in range(len(nums)):
    
            total_pairs += freq[nums[right]]
            freq[nums[right]] += 1
            
            while total_pairs >= k:
                res += len(nums) - right
                total_pairs -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1
        
        return res