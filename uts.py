def calculate_hash(data, array_dimension):
    ascii = ord(data['name'][0])
    calculated_hash = ascii % array_dimension
    return calculated_hash


def append_h(h_array, data):
    for h_index in range(len(h_array)):
        if h_array[h_index] == None:
            h_array[h_index] = data
            return h_array


def is_full(array_2d, data):
    arr_length = len(array_2d)
    v_index = calculate_hash(data, arr_length)
    hz_array = array_2d[v_index]
    for hz_index in range(0, len(hz_array) + 1):
        if hz_index == len(hz_array):
            return (v_index, True)
        elif hz_array[hz_index] == None:
            return (v_index, False)


def resize(h_array, new_size):
    new_h_array = [None] * new_size
    for dict in h_array:
        new_h_array = append_h(new_h_array, dict)
    return new_h_array


def append(array_2d, data):
    (v, ToF) = is_full(array_2d, data)
    arr_length = len(array_2d)
    v_index = calculate_hash(data, arr_length)
    hz_array = array_2d[v_index]
    if ToF:
        old_size = len(hz_array)
        new_h_arr_size = 2 * old_size
        hz_array = resize(hz_array, new_h_arr_size)
        hz_array[old_size] = data
        array_2d[v_index] = hz_array
        return array_2d
    else:
        hz_array = append_h(hz_array, data)
        array_2d[v_index] = hz_array
        return array_2d


def search(array_2d, data):
    arr_length = len(array_2d)
    v_index = calculate_hash(data, arr_length)
    hz_array = array_2d[v_index]
    for hz_index in range(0, len(hz_array)):
        dict = hz_array[hz_index]
        if hz_array[hz_index] == None:
            return ((None, None), None)
        elif dict['name'] == data['name'] and dict['BoY'] == data['BoY']:
            return ((v_index, hz_index), dict)
    return ((None, None), None)


def selection(array_2d, choice):
    if choice == '1':
        while True:
            print()
            print('-' * 29)
            print(f"{'Mein Telefonbuch':^29}")
            print('-' * 29)
            print("\nAdd new data\n")
            name = (input(f"{'Name':18}: ")).lower()
            birth = input(f"{'Birth of Year':18}: ")
            if name == '' and birth == '':
                phone_number = input(f'{"Phone Number":18}: ')
                break
            else:
                dict = {'name': name, 'BoY': birth}
                ((v, h), data) = search(array_2d, dict)
                if data != None:
                    print("Phone Number: Can't add data. Already exists.")
                else:
                    phone_number = input(f'{"Phone Number":18}: ')
                    dict = {'name': name, 'BoY': birth, 'phone': phone_number}
                    append(array_2d, dict)
                    break
    elif choice == '2':
        print()
        print('-' * 29)
        print(f"{'Das Telefonbuch':^29}")
        print('-' * 29)
        print(f"\nSearch by name\n")
        name = (input(f"{'Name':18}: ")).lower()
        birth = input(f"{'Birth of Year':18}: ")
        dict = {'name': name, 'BoY': birth}
        if name == '' and birth == '':
            pass
        else:
            ((v, h), data) = search(array_2d, dict)
            if data != None:
                print(f"{'Phone Number':18}: {data['phone']}")
            else:
                print(f"{'Phone Number':18}: Not Found!")
    else:
        print(f"Wrong input, please try again.")


def should_return_same_hash():
    test_array = [[None, None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
    array_dimension = len(test_array)
    data1 = {'name': 'alpha'}
    data2 = {'name': 'mikha'}
    hash1 = calculate_hash(data1, array_dimension)
    hash2 = calculate_hash(data2, array_dimension)
    current = hash1
    expected = hash2
    assert expected == current


def should_return_different_hash():
    test_array = [[None, None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
    array_dimension = len(test_array)
    data1 = {'name': 'alpha'}
    data2 = {'name': 'beta'}
    current = calculate_hash(data1, array_dimension)
    expected = calculate_hash(data2, array_dimension)
    assert expected != current


def should_add_new_data():
    test_array = [[None, None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
    data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    append(test_array, data)
    current = test_array[1][0]
    expected = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    assert expected == current


def should_add_new_data_and_resize():
    test_array = [[None, None, None, None],
                  [{'name': 'alvin', 'BoY': '1978', 'phone': '0812398741'},
                   {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'},
                   {'name': 'mikhael', 'BoY': '2008', 'phone': '0812987234'},
                   {'name': 'michael', 'BoY': '2022', 'phone': '0812092834'}],
                  [None, None, None, None],
                  [None, None, None, None]]
    data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    append(test_array, data)
    current = test_array[1][4]
    expected = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    assert expected == current


def should_return_data_with_v_and_h_index():
    test_array = [[None, None, None, None],
                  [{'name': 'ina','BoY': '2001','phone': '081167896854'}, None, None, None],
                  [None, None, None, None],
                  [None, None, None, None]]
    data = {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'}
    current = search(test_array, data)
    expected = ((1, 0), {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'})
    assert expected == current


def should_not_return_data():
    test_array = [[None, None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
    data = {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'}
    current = search(test_array, data)
    expected = ((None, None), None)
    assert expected == current


def should_get_new_horizontal_array_with_new_length_2times_after_insert():
    test_array = [[None, None, None, None],
                  [{'name': 'alvin', 'BoY': '1978', 'phone': '0812398741'},
                   {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'},
                   {'name': 'mikhael', 'BoY': '2008', 'phone': '0812987234'},
                   {'name': 'michael', 'BoY': '2022', 'phone': '0812092834'}],
                  [None, None, None, None],
                  [None, None, None, None]]
    data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    append(test_array, data)
    current = len(test_array[1])
    expected = 8
    assert expected == current


def should_return_array_2d_with_the_same_length_like_before_insert():
    test_array = [[None, None, None, None],
                  [{'name': 'alvin', 'BoY': '1978', 'phone': '0812398741'},
                   {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'},
                   {'name': 'mikhael', 'BoY': '2008', 'phone': '0812987234'}, None],
                  [None, None, None, None],
                  [None, None, None, None]]
    data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    append(test_array, data)
    current = len(test_array[1])
    expected = 4
    assert expected == current


def should_return_true_when_array_full():
    test_array = [[None, None, None, None],
                  [{'name': 'alvin', 'BoY': '1978', 'phone': '0812398741'},
                   {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'},
                   {'name': 'mikhael', 'BoY': '2008', 'phone': '0812987234'},
                   {'name': 'michael', 'BoY': '2022', 'phone': '0812092834'}],
                  [None, None, None, None],
                  [None, None, None, None]]
    data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
    (v_index, current) = is_full(test_array, data)
    expected = True
    assert expected == current


def should_return_false_when_array_is_not_full():
  test_array = [[None, None, None, None],
                  [{'name': 'alvin', 'BoY': '1978', 'phone': '0812398741'},
                   {'name': 'ina', 'BoY': '2001', 'phone': '081167896854'},
                   {'name': 'mikhael', 'BoY': '2008', 'phone': '0812987234'},None],
                  [None, None, None, None],
                  [None, None, None, None]]
  data = {'name': 'mikha', 'BoY': '2002', 'phone': '0812080812'}
  (v_index, current) = is_full(test_array, data)
  expected = False
  assert expected == current


def test():
    print("Running tests...")
    should_return_same_hash()
    should_return_different_hash()
    should_add_new_data()
    should_add_new_data_and_resize()
    should_return_data_with_v_and_h_index()
    should_not_return_data()
    should_get_new_horizontal_array_with_new_length_2times_after_insert()
    should_return_array_2d_with_the_same_length_like_before_insert()
    should_return_true_when_array_full()
    should_return_false_when_array_is_not_full()
    print("Tests finished.")


def main():
    telephone_book = [[None, None, None, None], [None, None, None, None],
                      [None, None, None, None], [None, None, None, None]]
    while True:
        print()
        print('-' * 29)
        print(f"{'Mein Telefonbuch':^29}")
        print('-' * 29)
        print("\n1. Add new number\n2. Search by name\n3. Exit\n")
        choice = input(f"{'Choice?':18}")
        if choice == "3":
            print("bye-bye")
            break
        selection(telephone_book, choice)


if __name__ == "__main__":
    test()
    main()