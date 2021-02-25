class Solution:
    def findMaxAverage(self, a: List[int], k: int) -> float:
        n = len(a)
        sum = 0

        win = a[0:k]
        print(win)
        for i in win:
            sum += i
        print(sum)
        max = sum/k

        i = 1
        j = k
        while(j < n):
            sum = sum - a[i-1] + a[j]
            if(max < sum/k):
                max = sum/k
            i += 1
            j += 1

        return max
        
