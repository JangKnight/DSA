from typing import List

def moveZerosToEnd(arr: List[int]) -> List[int]:
    new_arr = list()
    zero_cnt = 0
    for num in arr:
        if num:
            new_arr.append(num)
        else: zero_cnt += 1
    
    for i in range(zero_cnt):
        new_arr.append(0)
    
    return new_arr
        
    
# debug your code below
print(moveZerosToEnd([0, 1, 0, 3, 12]))