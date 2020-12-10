# O(n) -> Time | O(1) -> Space
class Solution:
    def countVowelStrings(self, n: int) -> int:
        li = [1, 1, 1, 1, 1]
        for i in range(n):
            sum = 0
            l = li
            for j in range(4, -1, -1):
                sum += li[j]
                l[j] = sum

        return li[0]
