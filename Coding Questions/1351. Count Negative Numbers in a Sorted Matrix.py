class Solution:
    def countNegatives(self, a: List[List[int]]) -> int:
        n = len(a)
        m = len(a[0])

        i = 0
        count = 0
        while(i<n):
            j = 0
            if(a[i][0] >= 0):
                while(j<m and a[i][j]>=0):
                    j += 1
                count += m-j
            else:
                count += m
            i += 1

        return count
