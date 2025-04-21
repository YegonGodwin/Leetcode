from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        prefix = [0] * (n + 1)
        min_prefix = 0
        max_prefix = 0
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + differences[i - 1]
            if prefix[i] < min_prefix:
                min_prefix = prefix[i]
            if prefix[i] > max_prefix:
                max_prefix = prefix[i]
        
        # The starting value x must satisfy:
        # x >= lower - min_prefix (to ensure x + prefix[i] >= lower for all i)
        # x <= upper - max_prefix (to ensure x + prefix[i] <= upper for all i)
        # Also, x must be within [lower, upper]
        x_min = max(lower, lower - min_prefix)
        x_max = min(upper, upper - max_prefix)
        
        if x_max < x_min:
            return 0
        return x_max - x_min + 1