print("Ruchit Bagade")
def shell_sort_distinct(arr):
    n = len(arr)
    div = 2
    gap = n // div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] >= temp:
                if arr[j - gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        index_to_delete = list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n // div


if __name__=='__main__':
    elements=[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    print(elements)
    shell_sort_distinct(elements)
    print(elements)