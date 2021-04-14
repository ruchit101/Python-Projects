print("Last Data structure of the playlist for now then build and practice thats it and then django framework")


def linear_search(number_list, num):
    for index, element in enumerate(number_list):
        if element == num:
            return index
    return -1


def binary_search(number_list, num):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        midnum = number_list[mid_index]
        if midnum == num:
            return mid_index
        if num > midnum:
            left_index = mid_index + 1
        if num <= midnum:
            right_index = mid_index - 1
    return -1
def binary_Search_recursive(number_list, num,left_index,right_index):
    if right_index< left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    if mid_index>len(number_list) or mid_index < 0:
        return -1
    midnum = number_list[mid_index]

    if midnum == num:
        return mid_index
    if num > midnum:
        left_index = mid_index + 1
    if num <= midnum:
        right_index = mid_index - 1
    return binary_Search_recursive(number_list,num,left_index,right_index)


if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    #print(linear_search(list1, 8))
    print(binary_search(numbers,15))
    #print(binary_Search_recursive(list1, 8,0,4))
