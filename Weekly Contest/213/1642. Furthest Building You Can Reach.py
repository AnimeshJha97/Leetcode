# O(nlogn) -> Time(heapify) | O(n) -> Space
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        maxHeap = []
        heapify(maxHeap)
        i = 0
        while i<n-1:
            if heights[i] >= heights[i+1]:
                i += 1
            else:
                diff = heights[i+1] - heights[i]
                if diff <= bricks:
                    bricks -= diff
                    i += 1
                    heappush(maxHeap, -1 * diff)
                elif ladders > 0:
                    if len(maxHeap)>0:
                        x = abs(maxHeap[0])
                        if x>diff:
                            bricks += x
                            heappop(maxHeap)
                            heappush(maxHeap, -1 * diff)
                            bricks -= diff
                    ladders -= 1
                    i += 1
                else:
                    break
        return i
