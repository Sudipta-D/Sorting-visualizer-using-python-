def selection_sort(input_list):
    for i in range(len(input_list)):
        # Assume the current index is the minimum
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j

        # Swap the minimum value with the current value
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

# Feel free to use any list of numbers
numbers = [5, 2, 4, 6, 1, 3]
selection_sort(numbers)
print(numbers)

