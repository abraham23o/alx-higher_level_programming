#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    count = 0
    for num in my_list[:x]:
        try:
            print("{:d}".format(num), end="")
            count += 1

        except IndexError:
            break

    print()
    return count
