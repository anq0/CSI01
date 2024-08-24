def find_closest_distance(arr):
    dist_arr = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            dist_arr.append(abs(arr[i]-arr[j]))
    return min(dist_arr)

print(find_closest_distance([1, 5, 3, 2]))
print(find_closest_distance([1, 5, 3, 2, 5]))
