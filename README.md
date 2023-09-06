# ISU-CS-302

Data Structures and Algorithms repository for the Fall 2023 semester at Indiana State University. This repository
contains source code examples aligned with the course syllabus.

## What You'll Find Inside

Source code for various data structures like linked lists, stacks, queues, trees, and graphs.
Algorithm implementations, including sorting and searching algorithms.
Additional resources like reading materials and links to online tutorials for further learning.

## How to Use This Repository

Clone the repository to your local machine using `git clone https://github.com/msorkhpar/ISU-CS-302` command or use it
on Codespace.

- Run the following in your terminal:

```shell
#!/usr/bin/env bash

python3 -m venv .venv
source ./.venv/bin/activate
python3 -m pip install --upgrade pip
find . -name "requirements.txt" -type f -exec ./.venv/bin/pip3 install -r '{}' ';'
```

- Navigate to the week or topic you're interested in.
- Explore the source code and exercises.

## Table of Contents

### Sorting Algorithms

- [Selection Sort, Lecture1, page 3](01_sorting/01_selection_sort.py)
- [Bubble Sort, Lecture1, page 12](01_sorting/02_bubble_sort.py)
- [Merge Sort, Lecture1, page 16](01_sorting/03_merge_sort.py)
- [Challenge, Lecture1, page 23](01_sorting/03_merge_sort.py)

### Linked List
- [Singly Linked List](02_linked_list/01_singly_linked_list.py)
- [Doubly Linked List](02_linked_list/02_doubly_linked_list.py)

### Binary Tree
- [Binary Tree](03_binary_tree/01_simple_binary_tree.py)


## External Resources
- Heap: https://www.cs.usfca.edu/~galles/visualization/Heap.html
## License

This repository is licensed under the MIT License - see
the [LICENSE](https://github.com/msorkhpar/ISU-CS-302/blob/main/LICENSE) file for details.

