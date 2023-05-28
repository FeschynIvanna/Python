from abc import ABC, abstractmethod
'''
abstract class
'''


class Pen(ABC):

    def __init__(self, id, color, brand, size):
        self.id = id
        self.color = color
        self.brand = brand
        self.size = size

    @abstractmethod
    def calculate_price(self):
        pass
