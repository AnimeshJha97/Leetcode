# O(n) -> Time | O(n) -> Space
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        a = [0 for i in range(n+1)]
        a[0] = 0
        if n>0:
            a[1] = 1
        i = 1
        while i <= n/2:
            a[2*i] = a[i]
            if i<=(n-1)/2:
                a[2*i + 1] = a[i] + a[i+1]
            i += 1
        return max(a)
