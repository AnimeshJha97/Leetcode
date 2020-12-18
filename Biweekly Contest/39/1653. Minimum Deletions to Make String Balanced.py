# O(n) -> Time | O(n) -> Space
class Solution:
    def minimumDeletions(self, s: str) -> int:
        s = list(s)
# To count te frequencies of 'a' and 'b'        
        dict = {}
        for ss in s:
            if ss in dict:
                dict[ss] += 1
            else:
                dict[ss] = 1
# If only one of the character is in the string, no change
        if len(dict) == 1:
            return 0

"""
 The logic is to compare number of a's and b's present in left and right side.
 Initially left values are 0 and right are the frequency of chcracter
 As we pass through the character from left to right, we push them to left
 side of our imaginary pointer and thus increasing their left value and
 decreasing the right value.

 ans stores the value of freq. of 'a' ans the maximum ans can be freq of 'a'
 in the condition that all 'a' are present on right of last 'b'

 Now, while travesring the given list, we first compare the value of ans with
 the sum of b_left and a_right and choose the minimum of both, which tell
 the number of deletions we need to make.

 In the end we select the minimum again to amke sure if the corner most 'a'
 and 'b' are taken in consideration.
"""
        a_left, b_left = 0, 0
        a_right, b_right = dict['a'], dict['b']

        ans = a_right

        for ss in s:
            ans = min(ans, b_left + a_right)
            if ss == 'a':
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1

        ans = min(ans, b_left + a_right)
        return ans
