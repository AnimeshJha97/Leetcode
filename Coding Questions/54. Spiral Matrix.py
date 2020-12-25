class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        l = []
        while(i<m and j<n):
            for s in range(j, n):
                l.append(matrix[i][s])
            i += 1

            for s in range(i, m):
                l.append(matrix[s][n-1])
            n -= 1

            if(i<m):
                for s in range(n-1, j-1, -1):
                    l.append(matrix[m-1][s])
                m -= 1

            if(j<n):
                for s in range(m-1, i-1, -1):
                    l.append(matrix[s][j])
                j += 1

        return l
