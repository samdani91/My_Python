def main():
    arr = list(map(int, input('Enter array elements: ').split()))
    insertion_sort(arr)
    print("Sorted array:", arr)


def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


if __name__ == '__main__':
    main()
