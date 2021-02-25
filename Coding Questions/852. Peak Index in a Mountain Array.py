class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        n = len(a)
        i, j = 0, n-1

        while(i<j):
            mid = i+(j-i)//2
            if(a[mid - 1] < a[mid] and a[mid] > a[mid+1]):
                return mid
            elif(a[mid-1] > a[mid]):
                j = mid
            else:
                i = mid+1
