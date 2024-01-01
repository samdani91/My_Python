def main():
    arr = list(map(int, input("Enter Array Elements:").split()))
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    j = left

    while j < right:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    i += 1
    arr[i], arr[right] = arr[right], arr[i]

    return i


if __name__ == "__main__":
    main()
