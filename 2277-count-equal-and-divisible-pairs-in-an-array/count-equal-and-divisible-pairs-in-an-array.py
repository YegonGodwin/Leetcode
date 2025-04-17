from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_indices = defaultdict(list)
        for index, num in enumerate(nums):
            value_indices[num].append(index)
        
        count = 0
        for indices in value_indices.values():
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count