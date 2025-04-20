from collections import defaultdict
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        for num in answers:
            freq[num] += 1
        
        total = 0
        for x, count in freq.items():
            groups = math.ceil(count / (x + 1))
            total += groups * (x + 1)
        
        return total