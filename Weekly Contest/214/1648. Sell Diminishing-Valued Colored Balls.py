# O(nlog(n)) -> Time | O(n) -> Space
class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        li = []
# Heapify the list to create a heap
        heapify(li)
# By default, heap is minHeap.
# To create a max heap, insert the -ive of elements.
# Later, when we extract the 0th index of the heap, we multiply it with -1
# so as to get maximum element.
        for k in inv:
            heappush(li, -1*k)
        sum = 0
        for i in range(orders):
            k = abs(heappop(li))
            sum += k
# Substracted 1 for k and pushed back to heap
            heappush(li, -(k-1))
        sum = sum % 1000000007
        return sum
