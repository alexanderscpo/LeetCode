class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = ['' for _ in range(numRows)]
        if numRows >= len(s) or numRows == 1:
            return s
        
        i = 0
        desc = True

        for ch in s:
            if desc:
                i += 1
            else:
                i -= 1
            if i == numRows:
                desc = False
            elif i == 1:
                desc = True
                
            matrix[i-1] += ch

        return ''.join(matrix)