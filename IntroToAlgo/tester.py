from codecs import make_identity_dict


def linear_search(list, target):
    # we need to scan each element in a list and compare the value to the target
    # if the list val is equal to the target, then we need to return the index at
    # which the value was located.
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def binary_search(list, target):
    # we need to assume the start and finish of the list, then get the midpoint
    # at the midpoint we compare 3 times, if equal, if less, and if greater, than
    # the target compared to midpoint
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1

def recursive_binary_search(list, target):
    # we need to create sublists of the list to shorten the search in halves,
    # similar to the binary search, but we now call the function itself
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        elif list[midpoint] > target:
            return recursive_binary_search(list[:midpoint - 1], target)
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1:], target)


def verify_linbin_search(result):
    if result is not None:
        print("The target was found at index:", result)
    else:
        print("The target was not found in the list...")

def verify_recursive_bin(result):
    print("The target was inside the list:", result)

list = [2,3,4,5,6,7,8,9,11,34,56,89,100]
result = linear_search(list, 100)
verify_linbin_search(result)

second_result = binary_search(list, 89)
verify_linbin_search(second_result)

third_result = recursive_binary_search(list, 11)
verify_recursive_bin(third_result)

