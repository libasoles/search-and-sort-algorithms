def binary_search(data, target):

    items_length = len(data)
    middle = int(items_length/2)
    sample = data[middle]

    if items_length == 1:
        return -1

    if sample == target:
        return target

    if target < sample:
        return binary_search(data[:middle], target)
    if target > sample:
        return binary_search(data[middle:], target)

    return -1
