def selection_sort(data):
    for pointer, pointer_value in enumerate(data):
        minimum = pointer
        sample = pointer + 1
        while sample < len(data):
            if data[sample] < data[minimum]:
                minimum = sample
            sample += 1
        switch(data, pointer, minimum)


def switch(data, a, b):
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp
