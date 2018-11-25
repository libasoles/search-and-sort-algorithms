def mergeSort(data):

    itemsLength = len(data)

    if itemsLength == 1:
        return data
    elif itemsLength == 2:
        return data if data[0] <= data[1] else list(reversed(data))

    middle = int(itemsLength / 2)

    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])

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
