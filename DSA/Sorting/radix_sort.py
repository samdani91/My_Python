def main():
    arr = list(map(int, input("Enter Array Elements:").split()))
    radix_sort(arr)
    print("Sorted Array:", arr)


def radix_sort(arr):
    max_val = max(arr)
    place = 1

    while max_val // place > 0:
        count_sort(arr, place)
        place *= 10


def count_sort(arr, place):
    size = len(arr)
    count = [0] * 10
    ans = [None] * size

    for i in range(size):
        count[(arr[i] // place) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        ans[count[(arr[i] // place) % 10] - 1] = arr[i]
        count[(arr[i] // place) % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = ans[i]


if __name__ == '__main__':
    main()
