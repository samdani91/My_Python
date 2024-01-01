def main():
    arr = list(map(int, input("Enter Array Elements: ").split()))
    selection_sort(arr)
    print("Sorted Array:", arr)


def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    main()
