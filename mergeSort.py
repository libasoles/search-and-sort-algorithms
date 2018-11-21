
unsortedData = [15, 3, 29, 43, 54, 12, 16, 10, 8, 45, 99, 32, 75]

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

result = mergeSort(unsortedData)
print("FINAL RESULT", result)