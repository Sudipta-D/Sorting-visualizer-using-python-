import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Install matplotlib using 'pip install matplotlib'
# For Linux, if needed, run: sudo apt-get install --reinstall libxcb-xinerama0

# Utility function to swap elements
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Bubble Sort Algorithm
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
            yield array

# Insertion Sort Algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j - 1)
            j -= 1
            yield array

# Quick Sort Algorithm
def quick_sort(array, low, high):
    if low >= high:
        return
    pivot = array[high]
    pivot_index = low
    for i in range(low, high):
        if array[i] < pivot:
            swap(array, i, pivot_index)
            pivot_index += 1
        yield array
    swap(array, high, pivot_index)
    yield array
    yield from quick_sort(array, low, pivot_index - 1)
    yield from quick_sort(array, pivot_index + 1, high)

# Selection Sort Algorithm
def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
            yield array
        if min_index != i:
            swap(array, i, min_index)
            yield array

# Merge Sort Algorithm
def merge_sort(array, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    yield from merge_sort(array, low, mid)
    yield from merge_sort(array, mid + 1, high)
    yield from merge(array, low, mid, high)
    yield array

def merge(array, low, mid, high):
    temp = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    temp.extend(array[i:mid + 1])
    temp.extend(array[j:high + 1])
    for i, val in enumerate(temp):
        array[low + i] = val
        yield array

# Heap Sort Algorithm
def heapify(array, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        swap(array, i, largest)
        yield array
        yield from heapify(array, n, largest)

def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        swap(array, 0, i)
        yield array
        yield from heapify(array, i, 0)

# Shell Sort Algorithm
def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for start in range(gap):
            yield from gap_insertion_sort(array, start, gap)
        gap //= 2

def gap_insertion_sort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        current_value = array[i]
        pos = i
        while pos >= gap and array[pos - gap] > current_value:
            array[pos] = array[pos - gap]
            pos -= gap
            yield array
        array[pos] = current_value
        yield array

# Counting Sort Algorithm
def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)
    for num in array:
        count[num] += 1
        yield array
    index = 0
    for i, freq in enumerate(count):
        for _ in range(freq):
            array[index] = i
            index += 1
            yield array

# User Input
n = int(input("Enter the number of elements: "))
print("\nSorting Algorithms:")
print("1. Bubble Sort\n2. Insertion Sort\n3. Quick Sort\n4. Selection Sort\n5. Merge Sort\n6. Heap Sort\n7. Shell Sort\n8. Counting Sort\n")
choice = int(input("Choose an algorithm: "))

# Generate Random Array
array = [i + 1 for i in range(n)]
random.shuffle(array)

# Select Sorting Algorithm
if choice == 1:
    title = "Bubble Sort"
    algorithm = bubble_sort(array)
elif choice == 2:
    title = "Insertion Sort"
    algorithm = insertion_sort(array)
elif choice == 3:
    title = "Quick Sort"
    algorithm = quick_sort(array, 0, n - 1)
elif choice == 4:
    title = "Selection Sort"
    algorithm = selection_sort(array)
elif choice == 5:
    title = "Merge Sort"
    algorithm = merge_sort(array, 0, n - 1)
elif choice == 6:
    title = "Heap Sort"
    algorithm = heap_sort(array)
elif choice == 7:
    title = "Shell Sort"
    algorithm = shell_sort(array)
elif choice == 8:
    title = "Counting Sort"
    algorithm = counting_sort(array)
else:
    print("Invalid choice. Exiting.")
    exit()

# Visualization Setup
fig, ax = plt.subplots()
ax.set_title(title)
bar_rects = ax.bar(range(len(array)), array, align="edge")
ax.set_xlim(0, n)
ax.set_ylim(0, int(n * 1.1))
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
operations = [0]

# Update Function for Animation
def update(array, rects, operations):
    for rect, val in zip(rects, array):
        rect.set_height(val)
    operations[0] += 1
    text.set_text(f"Operations: {operations[0]}")

# Animate and Show Plot
animation = anim.FuncAnimation(
    fig,
    update,
    fargs=(bar_rects, operations),
    frames=algorithm,
    interval=1,
    repeat=False,
    cache_frame_data=False
)
animation.save("sorting_visualization.gif", writer="pillow")
plt.show()
