def binary_array_to_number(arr):
    total = 0
    exponent = len(arr) - 1

    for binary_num in arr:
        if binary_num:
            total += pow(2, exponent)
        exponent -= 1

    return total


if __name__ == "__main__":
    print(binary_array_to_number([0, 0, 0, 1]))  # Output: 1
    print(binary_array_to_number([0, 0, 1, 0]))  # Output: 2
    print(binary_array_to_number([0, 1, 0, 1]))  # Output: 5
    print(binary_array_to_number([1, 0, 0, 1]))  # Output: 9
    print(binary_array_to_number([0, 0, 1, 0]))  # Output: 2
    print(binary_array_to_number([1, 1, 1, 1]))  # Output: 15

    # vary length of the binary array
    print(binary_array_to_number([1, 0, 1]))  # Output: 5
    print(binary_array_to_number([1, 0, 0, 0, 1]))  # Output: 17
