class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        i = 0
        n = len(a)
        maxF = float(-inf)
        maxN = 0
        while(i<n):
            maxN += a[i]
            if(maxN < a[i]):
                maxN = a[i]
            if(maxF < maxN):
                maxF = maxN
            i += 1
        return maxF
