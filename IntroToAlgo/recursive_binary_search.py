def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1:], target)
        elif list[midpoint] > target:
            return recursive_binary_search(list[:midpoint], target)
def verify(result):
    print("The target was found:", result)

list = [1,2,3,4,5,6,7,8,9]
result = recursive_binary_search(list,9)
verify(result)

#////////////////////////////////////////////////////////////////#

def linear_search(list,target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify_linear_binary(result):
    if result is not None:
        print("Target what found at index:", result)
    else:
        print("Target was not found")
result = linear_search(list, 7)
verify_linear_binary(result)

#////////////////////////////////////////////////////////////////#

def binary_search(list, target):
    start = 0
    final = len(list) - 1

    while start <= final:
        midpoint = (start + final)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            start = midpoint + 1
        elif list[midpoint] > target:
            final = midpoint - 1
    return None

result = binary_search(list, 8)
verify_linear_binary(result)