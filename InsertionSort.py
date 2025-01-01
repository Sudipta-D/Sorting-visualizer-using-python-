def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i - 1
        next_element = input_list[i]

        while j >= 0 and input_list[j] > next_element:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = next_element

numbers = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(numbers)
print(numbers)
