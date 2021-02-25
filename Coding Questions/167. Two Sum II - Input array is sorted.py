class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        i, j = 0, len(a)-1
        while(i<j):
            if a[i]+a[j] == target:
                return [i+1, j+1]
            elif(a[i]+a[j] > target):
                j -= 1
            else:
                i += 1
