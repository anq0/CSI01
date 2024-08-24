def find_mode(arr):
    dict = {}
    mode_count = 0
    mode_arr = []
    for i in list(set(arr)):
        dict[i] = arr.count(i)
        if arr.count(i) > mode_count:
            mode_count = arr.count(i)
    if mode_count != 1:
        for i in dict:
            if dict[i] == mode_count:
                mode_arr.append(i)
        return max(mode_arr)
    
print(find_mode([1,2,3,22,22]))