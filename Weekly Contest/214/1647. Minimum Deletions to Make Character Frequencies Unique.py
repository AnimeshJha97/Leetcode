# O(n) -> Time | O(n) -> Space

class Solution:
    def minDeletions(self, s1: str) -> int:
# To store frequency of characters in string
        dict = {}
        for s in s1:
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
# To store frequency of characters in list
        li = []
        for s in dict:
            li.append(dict[s])
# To store frequency of frequencies stored in list
        dict = {}
        for s in li:
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
# Function that count te number of deletions
        def cc(d1, c):
            d2 = d1.copy()      # Copied the dictionsry of frequency of frequencies
            for s in d1:        # to preserve it for comparision to stop recursion
                if d1[s] > 1:
                    d2[s] -= 1
                    if s-1 > 0:
                        if s-1 in d2:
                            d2[s-1] += 1
                        else:
                            d2[s-1] = 1
                    c += 1
# If no changes in the dictionary, i.e., no deletion, return the counter c
            if d1 == d2:
                return c
# Else recursive call the function cc()
            else:
                return cc(d2, c)

        count = cc(dict, 0)
        return count
