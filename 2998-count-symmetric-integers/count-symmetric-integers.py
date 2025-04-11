class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            if length % 2 != 0:
                continue
            half = length // 2
            first_half = s[:half]
            second_half = s[half:]
            sum_first = sum(int(d) for d in first_half)
            sum_second = sum(int(d) for d in second_half)
            if sum_first == sum_second:
                count += 1
        return count