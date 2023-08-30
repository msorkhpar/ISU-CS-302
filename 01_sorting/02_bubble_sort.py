from utils.loader import load_base_configs


def swap(arr, i, j):
    """
    Swap elements in an array
    """
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort_algo(arr, n) -> list:
    """
    Bubble sort algorithm
    1. for (i = 1; i < n; i + + )
    2.      for (j = 1; j <= n − i ; j + +)
    3.          if (A[j + 1] < A[j ])
    4.              SWAP(A[j ], A[j + 1]);
    """
    for i in range(0, n):
        for j in range(i, n - i - 1):
            if arr[j + 1] < arr[j]:
                swap(arr, j, j + 1)
    return arr


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f'Unsorted array: {arr}')
    sorted_arr = bubble_sort_algo(arr, len(arr))
    logger.info(f'Sorted array: {sorted_arr}')
