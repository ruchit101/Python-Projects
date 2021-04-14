def selection_sort(arr,key1,key2=None):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j][key1] < arr[min_index][key1]:
                min_index = j
            if arr[j][key1] == arr[min_index][key1]:
                if arr[j][key2] < arr[min_index][key2]:
                    min_index = j
        if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]



if __name__ == '__main__':

    elements=[{'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    selection_sort(elements,'First Name','Last Name')
    print(elements)