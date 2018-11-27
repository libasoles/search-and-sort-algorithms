def insertion_sort(data, pointer=1):

    if pointer == len(data):
        return data

    sample = data[pointer]
    previous_pointer = pointer-1
    while previous_pointer >= 0 and sample < data[previous_pointer]:
        data[previous_pointer+1] = data[previous_pointer]
        previous_pointer = previous_pointer-1
    data[previous_pointer+1] = sample

    return insertion_sort(data, pointer+1)
