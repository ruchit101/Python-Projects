def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index

def insert_to_sorted(arr,key):
    index=place_to_insert(arr,key)
    return arr[:index]+[key]+arr[index:]

if __name__=='__main__':
    elements=[2,1,5,7,2,0,5]
    stream =[]

    count =0
    while(True):
        i=(i for i in elements)
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count) // 2]}")
        else:
            i1 = count // 2
            i2 = (count // 2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2]) / 2}")
