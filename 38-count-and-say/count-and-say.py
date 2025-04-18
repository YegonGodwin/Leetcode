class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        result = []
        i = 0
        while i < len(prev):
            current_char = prev[i]
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            result.append(f"{count}{current_char}")
            i += 1
        return ''.join(result)