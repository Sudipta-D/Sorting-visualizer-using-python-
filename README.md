# Sorting Algorithms using python 
This repository serves as a practical guide to understanding and implementing sorting algorithms, offering visualizations and code examples for each method. Explore and enhance your grasp of algorithm design and performance optimization.
# Selection Sort
Selection Sort is a straightforward algorithm that often outperforms Bubble Sort in terms of efficiency. It divides the input array into two sublists: one containing sorted elements and the other containing unsorted elements. During each iteration, the smallest element from the unsorted sublist is selected and placed at the end of the sorted sublist. This process continues until the entire array is sorted.
           ![enter image description here](https://www.lavivienpost.net/wp-content/uploads/2022/01/selection-600.gif)
       

>     to see the code open/run SelectionSort.py
>     Python3 SelectionSort.py

##  Insertion Sort
Insertion Sort is both faster and simpler than Bubble Sort and Selection Sort. It mimics the way people often sort playing cards. The algorithm iteratively removes one element from the unsorted list, finds its correct position in the sorted sublist, and inserts it. This process is repeated until all elements are sorted.
![enter image description here](https://www.lavivienpost.net/wp-content/uploads/2022/01/insertion-600.gif)

    > to see the code open/run InsertionSort.py
    > Python3 InsertionSort.py

##  Merge Sort
Merge Sort is an elegant example of a Divide and Conquer algorithm. It works in two phases:

1. Divide: Recursively divide the unsorted array into subarrays, each containing a single element.

2. Conquer: Merge the subarrays in a sorted manner, combining them into progressively larger arrays until the original array is fully sorted.
![enter image description here](https://www.lavivienpost.net/wp-content/uploads/2022/02/merge-sort-400.gif)

>     > to see the code open/run MergeSort.py
>     > Python3 MergeSort.py

## Quick Sort

Quick Sort is another Divide and Conquer algorithm that selects a pivot element and partitions the array around it. Elements smaller than the pivot are placed on one side, and elements larger are placed on the other. The process is repeated recursively for the subarrays. Various pivot selection strategies include:

1. Picking the first element.
2. Picking the last element (used in the implementation below).
3. Picking a random element.
4. Picking the median.

![enter image description here](https://www.lavivienpost.net/wp-content/uploads/2022/02/quicksort-600-1.gif)
>     > to see the code open/run QuickSort.py
>     > Python3 QuickSort.py

