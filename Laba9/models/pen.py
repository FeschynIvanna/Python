from abc import ABC, abstractmethod
'''
The Pen class represents a pen with specified properties.
'''


class Pen(ABC):

    def __init__(self, id, color, brand, size):
        """
        Initializes an instance of the Pen class with the given properties
        :param id:The unique identifier of the pen.
        :param color:The color of the pen.
        :param brand:The brand of the pen.
        :param size:The size of the pen.
        """
        self.id = id
        self.color = color
        self.brand = brand
        self.size = size
        self.pattern = None

    def dir_list(self, value=None):
        if value is not None:
            mydict = {k: v for k, v in self.dict.items() if isinstance(value, value)}
            print(mydict)

    def iter(self):
        yield from self.dict.items()

    @abstractmethod
    def calculate_price(self):
        """
        A method for calculating the price of a pencil case
        """
        pass

    # def dictionary_list(self, value_type=None):
    #     print('dictionary_list')
    #     if value_type is not None:
    #         person_dict = {key: value for key, value in self.__dict__.items() if isinstance(value, value_type)}
    #         print(person_dict)

