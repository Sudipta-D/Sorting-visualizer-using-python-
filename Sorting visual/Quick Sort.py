def partition(array, low, high):
    i = low - 1 
    pivot = array[high] 

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(array, low, high)

        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

numbers = [6, 5, 4, 1, 8, 7, 3, 4]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
