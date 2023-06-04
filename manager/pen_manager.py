from typing import List

from decorator.pen_decorator import log_arguments_to_file, log_exceptions_to_file
from models.pen import Pen


class PenManager:

    def __init__(self):
        self.pens: List[Pen] = []

    def __len__(self):
        return len(self.pens)

    def __getitem__(self, item):
        return self.pens.append(item)

    def __iter__(self):
        return iter(self.pens)

    @log_arguments_to_file("arguments.log")
    def list_of_size(self):
        print("list_of_size")
        size_list = [pen.size for pen in self.pens]
        return size_list

    @log_exceptions_to_file('exceptions.log')
    def indexed_list(self):
        print("Indexed_list:")
        for index, pen in enumerate(self.pens):
            print(index + 1, pen)

    @log_exceptions_to_file("exceptions.log")
    def numeric_list(self):
        print("Numeric_list:")
        for object, function in zip(self.pens, self.list_of_size()):
            print(object, function)

    @log_exceptions_to_file("exceptions.log")
    def check_condition_all_any(self, value):
        print("All and Any:")
        all_satisfy = all(pen.size > value for pen in self.pens)
        any_satisfy = any(pen.size > value for pen in self.pens)
        return {"all": all_satisfy, "any": any_satisfy}

    @log_arguments_to_file("arguments.log")
    @log_exceptions_to_file("exceptions.log")
    def add_pen(self, new_pen):
        self.pens.append(new_pen)

    @log_arguments_to_file("arguments.log")
    @log_exceptions_to_file("exceptions.log")
    def add_pens(self, pens):
        self.pens.extend(pens)

    @log_arguments_to_file("arguments.log")
    @log_exceptions_to_file("exceptions.log")
    def find_all_the_bigger_than(self, size):
        """
        Find all pencil cases larger than this size
        """
        print("Pens the biggest: ")
        for pen in self.pens:
            if pen.size > size:
                print(pen)

    @log_arguments_to_file("arguments.log")
    @log_exceptions_to_file("exceptions.log")
    def find_by_color(self, color):
        """
        Find a pencil case by this color
        """
        print("Pens with this color: ")
        for pen in self.pens:
            if pen.color == color:
                print(pen)
