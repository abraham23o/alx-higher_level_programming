#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        res = 0
        try:
            res = my_list_1[num] / my_list_2[num]

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        finally:
            result.append(res)

    return result
