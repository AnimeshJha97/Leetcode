# O(n) -> Time | O(1) -> Space

class Solution:
    def longestMountain(self, a: List[int]) -> int:
        n = len(a)
        if n < 3:
            return 0

        valley = False
        peak = False

        res = 0
        i = 0

        while(i < n-1):
            if a[i] < a[i+1]:
                start = i
                while i < n-1 and a[i] < a[i+1]:
                    i += 1
                    peak = True
                while i < n-1 and a[i] > a[i+1]:
                    i += 1
                    valley = True

                if peak and valley:
                    res = max(res, i-start+1)

                peak = False
                valley = False

            else:
                i += 1
        return res
