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

def filther_not_equal(arr, value):
            new_lst = []

            for i in range(0, len(arr)):
                if arr[i] != value:
                    new_lst.append(arr[i])
    
                print(f"Массив с элементами не равные value: {new_lst}")
                return new_lst

def test():
      filter_greather([4, 3, 2, 12], 3)

      filther_less([2, 3, 4, 5], 3)

      filther_equal([2, 3, 4, 66], 66)

      filther_not_equal([3, 2, 1], 1)
print(test())