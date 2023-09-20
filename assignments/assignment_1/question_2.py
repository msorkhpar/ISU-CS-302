from utils.loader import load_base_configs

logger = None


def is_valid(arr):
    last_odd_index = first_even_number = -1
    for i, x in enumerate(arr):
        if x % 2 == 0 and first_even_number == -1:
            first_even_number = i
        elif x % 2 == 1:
            last_odd_index = i
    return last_odd_index < first_even_number


def permutation(arr, i, n):
    if i == n and is_valid(arr):
        print(",".join(map(str, arr)))
        return

    for t in range(i, n):
        # exchange Array[i], Array[t]
        arr[i], arr[t] = arr[t], arr[i]
        permutation(arr, i + 1, n)
        # exchange back Array[t], Array[i]
        arr[i], arr[t] = arr[t], arr[i]


def main():
    global logger
    env, logger = load_base_configs()
    n = int(input("Enter a non-negative number: "))
    if n >= 0:
        permutation([i + 1 for i in range(n)], 0, n)
    else:
        logger.error("Invalid input")


if __name__ == '__main__':
    main()
