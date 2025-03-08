# Sorting Performance Analyzer

## Description
This Python program generates a list of 1000 random integers and applies two sorting algorithms—Bubble Sort and Insertion Sort—to analyze their performance. It measures execution time for each sorting method and displays the results.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Classes](#classes)
- [Requirements](#requirements)
- [License](#license)

## Features
- Generates a list of 1000 random integers (values between 1 and 100).
- Implements **Bubble Sort** and **Insertion Sort** for performance comparison.
- Measures and displays execution time for each sorting algorithm.
- Uses `doctest` for verification of sorting functionality.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/sorting-analyzer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd sorting-analyzer
   ```
3. Ensure Python 3.x is installed on your system.

## Usage
1. Run the script:
   ```sh
   python sorting_analyzer.py
   ```
2. The program will generate a list, apply both sorting algorithms, and display execution times.

## Example Output
```sh
The time of executing bubble sort of list A is: 45.231ms
The time of executing insertion sort of list A is: 31.784ms
```

## Classes
### `GeneratedList`
- **Method:** `listCreation()`
- **Description:** Generates a list of 1000 random integers (values between 1 and 100).

### `SortMethods`
- **Method:** `bubble_sort(arr, name)`
  - Sorts a list using **Bubble Sort**.
  - Measures execution time and prints the results.
- **Method:** `insertion_sort(arr, name)`
  - Sorts a list using **Insertion Sort**.
  - Measures execution time and prints the results.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
