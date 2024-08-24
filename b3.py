def has_sequence_with_sum(target_sum, arr):
    has_sum = False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j+1]) == target_sum:
                has_sum = True
    return has_sum

print(has_sequence_with_sum(15,[1,2,3,4,5]))



