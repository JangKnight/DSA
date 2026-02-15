def search(self, arr, target_sum):
    i, j = 0, len(arr) - 1
    while i < j:
        if target_sum == (arr[i] + arr[j]):
            return [i, j]
        elif target_sum < (arr[i] + arr[j]):
            print((arr[i] + arr[j]))
            j -= 1
        else:
            print((arr[i] + arr[j]))
            i += 1
    return [-1, -1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    target_sum = 6
    print(search(arr, target_sum))