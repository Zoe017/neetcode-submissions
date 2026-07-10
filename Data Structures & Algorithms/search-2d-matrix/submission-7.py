class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = 0
        n = len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                if target <= matrix[m][n]:
                    break
                l = m + 1
            else:
                return True
        
        R = len(matrix[0])
        L = 0
        while L <= R:
            M = L + (R - L) // 2
            if M < 0 or M > len(matrix[0]) - 1:
                return False
            if target < matrix[m][M]:
                R = M - 1
            elif target > matrix[m][M]:
                L = M + 1
            else:
                return True
        return False

