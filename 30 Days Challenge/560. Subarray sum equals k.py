# Subarray Sum equals k

li = input()
li = list(map(int, li.split(' ')))
k = int(input())
count = 0
sum = 0

# Using List -> prefixSum
# O(n) -> Time | O(n) -> Space
prefixSum = []
for i in range(len(li)):
    if i == 0:
        prefixSum.append(li[i])
        if li[i] == k:
            count += 1
    else:
        sum += li[i]
        if li[i] == k:
            count += 1
        elif (sum - k) in prefixSum:
            count += 1
        prefixSum.append(sum)
print(count)

# Using Dictionary/Map:
prefixSum = {}
count = 0
sum = 0
for i in range(len(li)):
    sum += li[i]
    if sum == k:
        count += 1

print(count)
