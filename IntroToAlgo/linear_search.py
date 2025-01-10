# def linear_search(my_list, target):
#     for index in range(0,len(my_list)):
#         if my_list[index] == target:
#             return index
#     return None
#
# def verify(index):
#     if index is not None:
#         print("Target found at index: ", index)
#     else:
#         print("Target not in list")
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
# result = linear_search(numbers, 10)
# verify(result)



def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            print(f"The target was found at index: {i}")
        elif list[i] is None:
            print("Target not found")
my_list = [1,2,3,4,5]
linear_search(my_list, 2)
















