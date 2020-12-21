"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
# O(n) -> Time | O(1) -> Space
def isMonotonic(self, A: List[int]) -> bool:
    n = len(A)
    j = 0

# Check if any repeating integers in the end, and get to the last repeating integer
    while j < n-1 and A[j] == A[j+1]:
        j += 1

# If all the elements are equal, return true
    if j == n-1:
        return True

# If not, compare the jth element with (j+1)th element
# If next element smaller, check if all are in decreasing order
# else check if all are in increasing order.
    if A[j] < A[j+1]:
        for i in range(j,n-1):
            if A[i] > A[i+1]:
                return False
    elif A[j] > A[j+1]:
        for i in range(j,n-1):
            if A[i] < A[i+1]:
                return False
    return True
