from utils.loader import load_base_configs


def merge(arr1, arr2):
    """
    Merge( A, B )
    1. int i=1; int j=1; int k=1;
    2. int n=size(A); int m=size(B); int C[m+n];
    3. while (k <= m + n ){
    4. if (A[i ] < B [j ], i <= n, j <= m)
    5. C [k ] := A[i ]; i + +; k + +;
    6. if (B [j ] <= A[i ], i <= n, j <= m)
    7. C [k ] := B [j ]; j + +; k + +;
    8. if (j < m)
    9. for (; j <= m; j + +) {
    10. C[k]:=B[j]; k++;
    11.}
    12. if (i < n)
    13. for (; i <= n; i + +) {
    14. C[k]:=A[i]; k++;
    15. }
    16. Return C;
    """
    i, j, k = 0, 0, 0
    n, m = len(arr1), len(arr2)
    merged_array = [0] * (m + n)
    while k < m + n:
        if i < n and j < m:
            if arr1[i] < arr2[j]:
                merged_array[k] = arr1[i]
                i += 1
            else:
                merged_array[k] = arr2[j]
                j += 1
        elif i == n:
            merged_array[k] = arr2[j]
            j += 1
        elif j == m:
            merged_array[k] = arr1[i]
            i += 1
        k += 1

    return merged_array


def merge_sort_algo(arr, left, right) -> list:
    """
    Merge sort algorithm

    Merge-Sort (A[left:right] ){
    1. if( left== right )
    Return A
    2. int middle = (left + right )/2; // integer division
    3. A1=Merge-Sort (A[left : middle] )
    4. A2=Merge-Sort (A[middle+1 :right] )
    5. C[1,right-left+1]= Merge ( A1,A2);
    6. for (i = 0; i <= right − left ; i + +)
    7. A[left+i] := C[i+1];
    8. }
 """
    if left == right:
        return [arr[left]]
    middle = (left + right) // 2
    a1 = merge_sort_algo(arr, left, middle)
    a2 = merge_sort_algo(arr, middle + 1, right)
    c = merge(a1, a2)
    for i in range(0, right - left + 1):
        arr[left + i] = c[i]

    return arr[left:right + 1]


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f'Unsorted array: {arr}')
    sorted_arr = merge_sort_algo(arr, 0, len(arr)-1)
    logger.info(f'Sorted array: {sorted_arr}')
