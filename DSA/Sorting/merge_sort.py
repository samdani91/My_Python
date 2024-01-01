def main():
    arr = list(map(int, input("Enter Array Elements: ").split()))
    divide(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)


def divide(arr, low, high):
    if low == high:
        return
    mid = low + (high - low) // 2
    divide(arr, low, mid)
    divide(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp_list = []
    idx1 = low
    idx2 = mid + 1

    while idx1 <= mid and idx2 <= high:
        if arr[idx1] <= arr[idx2]:
            temp_list.append(arr[idx1])
            idx1 += 1
        else:
            temp_list.append(arr[idx2])
            idx2 += 1

    while idx1 <= mid:
        temp_list.append(arr[idx1])
        idx1 += 1
    while idx2 <= high:
        temp_list.append(arr[idx2])
        idx2 += 1

    k = low
    for i in range(len(temp_list)):
        arr[k] = temp_list[i]
        k += 1


if __name__ == '__main__':
    main()
