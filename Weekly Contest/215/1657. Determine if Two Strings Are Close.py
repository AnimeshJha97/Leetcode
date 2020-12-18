# O(n) -> Time | O(n) -> Space
# Saved some space by reusing old list
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = {}
        d2 = {}
        for k in word1:
            if k in d1:
                d1[k] += 1
            else:
                d1[k] = 1
        li = []
        for k in d1:
            li.append(d1[k])
        word1 = []
        for k in word2:
            if k in d2:
                if k in d1:
                    d2[k] += 1
                else:
                    return False
            else:
                d2[k] = 1
        for k in d2:
            word1.append(d2[k])
        li.sort()
        word1.sort()
        for i in range(len(li)):
            if li[i] != word1[i]:
                return False
        return True
