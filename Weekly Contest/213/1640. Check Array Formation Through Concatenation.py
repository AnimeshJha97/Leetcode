# Solution 1
# O(m*n^2) -> Time | O(1) -> Space
# m = size of pieces
# n = size of arr and worst case for size of each list in list piece
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0

        for m in range(0,len(pieces)):
            for k in pieces:
                if i < len(arr) and k[0] == arr[i]:
                    for l in k:
                        if l == arr[i]:
                            i+=1
                        else:
                            return False

        if i != len(arr):
            return False

        return True


# Solution 2
# O(n^2) -> Time | O(m) -> Space
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        startIndex = dict()

        for k in pieces:
            startIndex[k[0]] = k

        i = 0
        while i != len(arr):
            start = arr[i]
            
            if start not in startIndex:
                return False
            else:
                for k in startIndex[start]:
                    if k == arr[i]:
                        i+=1
                    else:
                        return False
        return True
