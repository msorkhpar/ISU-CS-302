from utils.loader import load_base_configs


def is_subsequence(a, b) -> bool:
    """
   We are given two sequences A and B (say sequence of some alphabet).
   We say A is a subsequence of B, if the letters in A appears in B from left to right and in the same order
    (not necessarily consecutive) as A.
     In other words, there are i1, i2,..., in (n is the length of A) such that A[1] == B [i1]; A[2] == B [i2]; ...;
     A[n] = B [in]. Write a code that takes two sequences A,B and outputs whether A is a subsequence of B or not.
    """
    i, j = 0, 0
    n = len(a)
    m = len(b)
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1

    return i == n


if __name__ == '__main__':
    env, logger = load_base_configs()
    seq1 = env.list('SEQ_1')
    seq2 = env.list('SEQ_2')
    logger.info(f'Sequences \n\tSEQ_1: {seq1},\n\tSEQ_2: {seq2}\n')
    if is_subsequence(seq1, seq2):
        logger.info(f'SEQ_1 is a subsequence of SEQ_2')
    else:
        logger.error(f'SEQ_1 is NOT a subsequence of SEQ_2')
