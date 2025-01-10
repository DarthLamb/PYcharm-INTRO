def linear_search(my_list, target):
    for index in range(0,len(my_list)):
        if my_list[index] == target:
            return index
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 10)
verify(result)