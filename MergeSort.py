def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)

def merge(left_half, right_half):
    result = []
    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            result.append(left_half.pop(0))
        else:
            result.append(right_half.pop(0))

    result.extend(left_half if left_half else right_half)
    return result

numbers = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(numbers))
