def filter_greather(arr, value):
    new_lst = []

    for element in arr:
        if element > value:
            new_lst.append(element)
    
    print(f"Массив с элементами больше value: {new_lst}")
    return new_lst

def filther_less(arr, value):
        new_lst = []

        for element in arr:
            if element < value:
                new_lst.append(element)
    
        print(f"Массив с элементами меньше value: {new_lst}")
        return new_lst

def filther_equal(arr, value):
            new_lst = []

            for element in arr:
                if element == value:
                    new_lst.append(element)
    
            print(f"Массив с элементами, которые равны value: {value}")
            return new_lst
