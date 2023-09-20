def nice_string(arr, i, difference, n):
    if i == n:
        if difference == 0:
            print(",".join(map(str, arr)))
        return
    if difference < 0:
        return

    if difference > n - i:
        return

    arr[i] = 0
    nice_string(arr, i + 1, difference - 1, n)

    arr[i] = 1
    nice_string(arr, i + 1, difference + 1, n)


def main():
    n = int(input("Enter a non-negative number: "))
    if n < 0:
        return
    arr = [0] * n
    nice_string(arr, 0, 0, n)


if __name__ == "__main__":
    main()
