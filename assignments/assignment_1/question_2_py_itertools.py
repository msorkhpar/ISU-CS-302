from itertools import permutations

from utils.loader import load_base_configs


def generate_permutations(n, logger):
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
    even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]

    odd_permutations = list(permutations(odd_numbers))
    even_permutations = list(permutations(even_numbers))

    for odd_perm in odd_permutations:
        for even_perm in even_permutations:
            logger.info(",".join(map(str, odd_perm + even_perm)))


def main():
    env, logger = load_base_configs()
    n = int(input("Enter a non-negative number: "))
    if n >= 0:
        generate_permutations(n, logger)
    else:
        logger.error("Invalid input")


if __name__ == '__main__':
    main()
