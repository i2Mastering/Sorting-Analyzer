"""
Sorting Performance Analyzer

This Python module generates a list of 1000 random integers and applies two sorting algorithms—Bubble Sort and Insertion Sort—to analyze their performance.

Classes:
    - GeneratedList: Creates a list of random integers.
    - SortMethods: Implements Bubble Sort and Insertion Sort with execution time tracking.

Example Usage:
    ```python
    python sorting_analyzer.py
    ```
    Output:
    ```
    The time of executing bubble sort of list A is: 45.231ms
    The time of executing insertion sort of list A is: 31.784ms
    ```

Author: Ike Iloegbu
License: MIT
"""

from datetime import datetime
import random, doctest

class GeneratedList:
    """Generates a list of 1000 random integer values ranging from 1 to 100."""
    
    @staticmethod
    def listCreation():
        """Creates and returns a list of random integers."""
        return [random.randrange(100) for _ in range(1000)]

class SortMethods(GeneratedList):
    """
    Implements sorting methods and measures their execution time.
    
    Sorting Methods:
        - bubble_sort(arr, name): Sorts a list using the Bubble Sort algorithm.
        - insertion_sort(arr, name): Sorts a list using the Insertion Sort algorithm.
    
    Example:
        >>> test_list = [5, 3, 7, 2]
        >>> sorted(test_list)
        [2, 3, 5, 7]
    """
    
    @staticmethod
    def bubble_sort(arr, name):
        """Sorts a list using the Bubble Sort algorithm and measures execution time."""
        n = len(arr)
        start = datetime.now()
        
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        
        end = datetime.now()
        execution_time = (end - start).total_seconds() * 10**3
        print(f"The time of executing bubble sort of {name} is: {execution_time:.03f}ms")
    
    @staticmethod
    def insertion_sort(arr, name):
        """Sorts a list using the Insertion Sort algorithm and measures execution time."""
        n = len(arr)
        start = datetime.now()
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        end = datetime.now()
        execution_time = (end - start).total_seconds() * 10**3
        print(f"The time of executing insertion sort of {name} is: {execution_time:.03f}ms")

if __name__ == "__main__":
    # Generate a random list and store it in listA
    listA = GeneratedList.listCreation()
    
    # Perform sorting and measure performance
    SortMethods.bubble_sort(listA.copy(), "list A")
    SortMethods.insertion_sort(listA.copy(), "list A")
    
    # Run doctests
    doctest.testmod()
