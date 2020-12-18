# O(n*k) -> Time | o(n) -> Sapce
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [None for i in range(n)]
        if k > 0:
            for i in range(n):
                sum = 0
                for j in range(1, k+1):
                    sum += code[(i+j)%n]
                ans[i] = sum
        elif k == 0:
            ans = [0 for i in range(n)]
        else:
            for i in range(n):
                sum = 0
                for j in range(1, -k+1):
                    sum += code[(i-j)%n]
                ans[i] = sum
        return ans

# Using Sliding Window Protocol
# O(n) -> Time | O(n) -> Space
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0 for i in range(n)]
        left, right = 1, k
        if k == 0:
            return ans
        elif k < 0:
            k = -k
            left , right = n-k, n-1
        total = sum(code[i] for i in range(left, right+1))
        for i in range(n):
            ans[i] = total
            total -= code[left%n]
            total += code[(right+1)%n]
            left += 1
            right += 1
        return ans
