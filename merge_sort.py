def merge_sort(data):
    items_length = len(data)

    if items_length == 1:
        return data
    elif items_length == 2:
        return data if data[0] <= data[1] else list(reversed(data))

    middle = int(items_length / 2)

    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    result = []
    j = 0
    for i,value in enumerate(left):
        while len(right) > j and right[j] <= left[i]:
            result.append(right[j])
            j += 1
        result.append(left[i])

    if j < len(right):
        result.extend(right[j:])
    return result
