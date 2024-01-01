def main():
    arr = list(map(int, input('Enter array elements:').split()))
    bubble_sort(arr)
    print('Sorted array:', arr)


def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    main()
