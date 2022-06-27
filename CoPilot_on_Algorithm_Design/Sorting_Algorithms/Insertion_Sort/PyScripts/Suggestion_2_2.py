


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == ""__main__"":
    test = [random.randint(0, 100) for _ in range(10)]
    print(insertion_sort(test))

