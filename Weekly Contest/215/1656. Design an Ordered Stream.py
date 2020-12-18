# O(n^2) -> Time | O(n) -> Space
class OrderedStream:

    def __init__(self, n: int):
        self.li = [None] * n
        self.pt = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.li[id-1] = value

        a = []
        while self.pt < len(self.li) and self.li[self.pt] is not None:
            a.append(self.li[self.pt])
            self.pt += 1
        return a


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
