a = "2, , , , ,,,,,,,,                        ,,,,               , 3"

test = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc"


def split_string(ranges_string, input_str):
    temp_list = list(filter(None, map(lambda x: None if x == '' else x, map(str.strip, ranges_string.split(",")))))
    try:
        if not (all(list(map(str.isdigit, map(str.strip, temp_list))))):
            raise ValueError(f"Invalid input {ranges_string}")
        if len(temp_list) != 2:
            raise ValueError(f"Length of array is other than expected: {len(temp_list)}, expected: 2")
        if int(temp_list[0]) > int(temp_list[1]):
            raise ValueError(f"Value {temp_list[1]} cannot be greater than {temp_list[0]}")
        if int(temp_list[0]) > len(input_str):
            raise ValueError(f"Range from {temp_list[0]} cannot be greater than length of string: {len(input_str)}")
    except ValueError as _ex:
        print(_ex)
    else:
        ranges = list(map(int, temp_list))
        if ranges:
            return input_str[ranges[0]:ranges[1] + 1]


end = split_string(a, test)
print(end)
