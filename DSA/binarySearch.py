def main():
    arr = []
    # size = int(input("Enter size of the array:"))

    print("Enter array elements:")
    # for i in range(size):
    #     ele = int(input())
    #     arr.append(ele)

    arr = list(map(int, input().split()))
    # print(arr)

    target = int(input("Enter element to be searched:"))

    index = binary_search(arr, 0, len(arr) - 1, target)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")


def binary_search(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, right, target)
        else:
            return binary_search(arr, left, mid - 1, target)
    else:
        return -1


if __name__ == "__main__":
    main()
