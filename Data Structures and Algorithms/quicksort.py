print("Complete Sorting today please It's highly recommended!! We have to start the Mechanical Project.")


# Divide and Conquer technique
# Two types of Partitioning we come across 1) Hoare Partition 2) Lomuto Partition
# Applying The Hoare partition scheme for these algorithm
# Lomuto might be in the Exercise  DOnt worry about the code understand it You have 90 days to practice Go kill ii

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


def partition(elements, start, end): # BRINGING THE PIVOT IN THE MIDDLE OF THE LIST.
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot: # we are searching BIG-start and SMALL-End.
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    print(elements)
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
