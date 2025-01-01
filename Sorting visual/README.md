Sorting algorithms come in various forms, and understanding their functionality can be challenging without proper visualization.

Pro Tip: Visualizations not only help in understanding how these algorithms work but also provide insights into their time complexities.

## Introduction
This repository serves as a demonstration of visualizing 8 different sorting algorithms. Its goal is to make these algorithms more accessible for programmers to understand. Additionally, it allows you to compare the time complexities of different sorting algorithms through dynamic visual representations.
| Sorting Algorithm | AverageTime Complexity | Bad Time Complexity | Stability |
| ----------------- | ---------------------- | ------------------- | --------- |
| Bubble Sort       | O(N^2)                 | O(N^2)              | YES       |
| Insertion Sort    | O(N^2)                 | O(N^2)              | YES       |
| Shell Sort        | O(N^5/4)               | O(N^2)              | NO        |
| Selection Sort    | O(N^2)                 | O(n^2)              | NO        |
| Heapify Sort      | O(NlogN)               | O(NlogN)            | NO        |
| Merge Sort        | O(NlogN)               | O(NlogN)            | YES       |
| Quick Sort        | O(NlogN)               | O(N^2)              | NO        |
| Count Sort        | O(N)                   | O(N)                | YES       |



## Dependencies

- python3.x
- matplotlib
- pygame

## Quick Start

0. Check all dependencies installed

      This command can help you install all the dependent packages

      `pip install -r requirements.txt`
      
2. Start sorting.py

   `python3 sorting.py`

   - `Enter the number of elements:`: choise a number
   - `Choose algorithm:`: Sorting Type. Choose one
	 1.Bubble 
	 2.Insertion 
	 3.Quick 
	 4.Selection 
	 5.Merge Sort 
	 6.Heapify 
	 7.Shell 
	 8.Count sort
	 
3. Start sorting.py

   `python3 QuickSort.py`

   - `Press “Enter” key:`: to Perform Visualization.
   - `Press “R” key:`: to generate new array.
      
#### All sortings are done on randomly generated arrays of size 40.

### Bubble Sort
Total operations = 780 

![bubble](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTdkeXQ5emZyZDJrMG5lMTIxZ3A2cTRtNzZnMXZrMGZ1YnJhOTJpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hIDzLYByAJYN3Dg91r/giphy.gif)

### Selection Sort
Total operations = 816

![selection](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWRvMzAxazZ5ZmdmdHA4a3dzYno3ZHpodG4zODQ3cTV0aTBlNHo0diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qp8h6e0H9OT1w7nGUF/giphy.gif)

### Insertion Sort
Total operations = 431

![Insertion](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnFrYzZuZWlrdDQ1d200dWhoamJydTBla2ZiOHVtMHBqNTBhZXk2NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8HP1qtOgIoto54pCd8/giphy.gif)

### Quick Sort
Total operations = 201

![quick](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm9uamliMWVrcmh3NDY0NnN5cHhvbWp3OHl0dHZpY25oZGRhNTk4eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UNHd00MHMzMSGZwJxh/giphy.gif)

### Merge Sort
Total operations = 255

![merge](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2hoY2xqejF4bXA1em5vcDNlMXR6cGh1c28wbmRhMXE0aG9qeGVtbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l8GEkXg2eRUJcacfGD/giphy.webp)
