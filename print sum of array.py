def _sum(arr):

    sum = 0

    for i in arr:
        sum = sum + i

    return (sum)

arr = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    arr.append(ele)  # adding the element

print(arr)

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sums
print('Sum of the array is ', ans)
