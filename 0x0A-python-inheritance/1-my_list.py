#!/usr/bin/python3
"""
prints a list in sorted order
"""


class MyList(list):
    # def __init__(self):
    #     super().__init__()

    def print_sorted(self):
        """
        prints a list in sorted order
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)

