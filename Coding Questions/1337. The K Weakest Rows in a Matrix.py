class Solution:
    class ans:
        def __init__(self, row, count):
            self.row = row
            self.count = count

    def binary(self,a: List[int]) -> int:
        i, j = 0, len(a)
        while(i<j):
            mid = i+(j-i)//2
            if(a[mid] == 1):
                i = mid+1
            else:
                j = mid
        return i

    def kWeakestRows(self, a: List[List[int]], k: int) -> List[int]:
        answer = []
        i = 0
        for li in a:
            count = self.binary(li)
            answer.append(self.ans(i, count))
            i += 1

        for i in range(0,len(answer)):
            for j in range(len(answer)-i-1):
                if(answer[j].count > answer[j+1].count):
                    temp = answer[j]
                    answer[j] = answer[j+1]
                    answer[j+1] = temp
        # for i in range(0,len(answer)):
        #     print(answer[i].row, answer[i].count, end = " // ")
        final = []
        for i in range(0,k):
            final.append(answer[i].row)

        return final
