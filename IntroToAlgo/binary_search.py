def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
        elif list[midpoint] == target:
            return midpoint

def verify(index):
    if index is not None:
        print("Your target is in the list at:", index)
    else:
        print("Your target is not in the list")

numbers = [1,2,3,4,5,6,7,8]
result = binary_search(numbers,1)
verify(result)