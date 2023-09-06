import heapq
from heapq import heappop, heapify

from utils.loader import load_base_configs


def heap_sort(arr):
    heapify(arr)
    return [heappop(arr) for _ in range(len(arr))]


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f'Unsorted array: {arr}')
    sorted_arr = heap_sort(arr)
    logger.info(f'Sorted array: {sorted_arr}')
