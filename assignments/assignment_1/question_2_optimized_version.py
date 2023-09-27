import math

from utils.loader import load_base_configs


def permutation(arr, i, j, n, logger):
    if n % 2 == 0:
        if i == n / 2 and j == n:
            logger.info(",".join(map(str, arr)))
            return
    else:
        if i == math.ceil(n / 2) and j == n:
            logger.info(",".join(map(str, arr)))
            return

    for t in range(i, math.ceil(n / 2)):
        for k in range(j, n):
            arr[i], arr[t] = arr[t], arr[i]
            arr[k], arr[j] = arr[j], arr[k]
            permutation(arr, i + 1, j + 1, n, logger)
            arr[i], arr[t] = arr[t], arr[i]
            arr[k], arr[j] = arr[j], arr[k]


def generate_permutations(n, logger):
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
    even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]
    array = list()
    for i in odd_numbers:
        array.append(i)
    for j in even_numbers:
        array.append(j)

    if n % 2 == 0:
        permutation(array, 0, math.ceil(n / 2), n, logger)
    else:
        permutation(array, 0, math.ceil(n / 2) - 1, n, logger)


def main():
    env, logger = load_base_configs()
    n = int(input("Enter a non-negative number: "))
    if n >= 0:
        generate_permutations(n, logger)
    else:
        logger.error("Invalid input")


if __name__ == '__main__':
    main()
