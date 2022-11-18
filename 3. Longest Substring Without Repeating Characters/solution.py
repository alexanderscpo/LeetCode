class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i, val_i in enumerate(s):
            substring = f'{val_i}'
            for val_j in s[i+1:]:
                if val_j in substring:
                    break
                substring += val_j

            if max_len < len(substring):
                max_len = len(substring)

        return max_len