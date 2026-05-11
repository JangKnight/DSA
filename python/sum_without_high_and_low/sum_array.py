def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    return sum(arr) - min(arr) - max(arr)


if __name__ == "__main__":
    print(sum_array([6, 2, 1, 8, 10]))  # 16
    print(sum_array([1, 1, 11, 2, 3]))  # 7
    print(sum_array([1, 1, 11, 2, 3, -1]))  # 6
    print(sum_array([]))  # 0
    print(sum_array([3]))  # 0
    print(sum_array([3, 5]))  # 0
