def main():
    arr = list(map(int, input("Enter Array Elements:").split()))
    print("Sorted Array:", count_sort(arr))


def count_sort(arr):
    size = len(arr)
    max_value = max(arr)
    count = [0] * (max_value + 1)
    ans = [None] * size

    for i in range(size):
        count[arr[i]] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        ans[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return ans


if __name__ == '__main__':
    main()
