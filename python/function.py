def binary_search(data, item, start_pos) :
    print('data: {0}, item: {1}, offset: {2}'.format(data, item, start_pos))
    size = len(data)
    if size == 0 : return None

    pivot = size // 2

    if data[pivot] == item : return pivot + start_pos
    elif item < data[pivot] : return binary_search(data[:pivot], item, start_pos)
    else : return binary_search(data[pivot + 1:], item, start_pos + pivot + 1)

def insertion_sort(data) :

    size = len(data)
    for i in range(1, size) :

        j = i
        while j > 0 and data[j] < data[j - 1] : 
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1

def split_char(str, char) :

    start_pos = 0
    size = len(str)
    splits = []
    for pos in range(size) :
        if str[pos] == char :
            splits.append(str[start_pos:pos])
            start_pos = pos + 1
    else :
        splits.append(str[start_pos:size])

    return splits

