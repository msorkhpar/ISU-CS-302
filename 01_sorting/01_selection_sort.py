from utils.loader import load_base_configs


def swap(arr, i, j):
    """
    Swap elements in an array
    """
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort_algo(arr, n) -> list:
    """
    Selection sort algorithm
    1. for (i = 1; i < n; i + + ){
    2.  element = A[i ]; int index = i ;
    3.      for (j = i + 1; j <= n; j + +) 4. if (A[j ] < element ) {
    5.          element = A[j ]; index = j ;
    6.      }
    7.      SWAP(A[i ], A[index ]);
    8. }
    """
    for i in range(0, n):
        index = i
        element = arr[i]
        for j in range(i + 1, n):
            if arr[j] < element:
                element = arr[j]
                index = j
        swap(arr, i, index)
    return arr


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f'Unsorted array: {arr}')
    sorted_arr = selection_sort_algo(arr, len(arr))
    logger.info(f'Sorted array: {sorted_arr}')
