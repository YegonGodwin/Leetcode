class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2) 
    
    def update(self, idx, delta=1):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos1 = {x: i for i, x in enumerate(nums1)}
        pos2 = {x: i for i, x in enumerate(nums2)}
        pairs = []
        for x in range(n):
            a = pos1[x]
            b = pos2[x]
            pairs.append((a, b, x))  

        left_counts = [0] * n
        sorted_left = sorted(pairs, key=lambda p: p[0])  

        fenwick_left = FenwickTree(n)
        for p in sorted_left:
            a, b, x = p
            left_count = fenwick_left.query(b) 
            left_counts[x] = left_count
            fenwick_left.update(b + 1)  
        
        right_counts = [0] * n
        sorted_right = sorted(pairs, key=lambda p: -p[0])  

        fenwick_right = FenwickTree(n)
        count = 0
        for p in sorted_right:
            a, b, x = p
            sum_le = fenwick_right.query(b + 1)  
            right_count = count - sum_le
            right_counts[x] = right_count
            fenwick_right.update(b + 1)
            count += 1
        
        total = 0
        for x in range(n):
            total += left_counts[x] * right_counts[x]
        return total