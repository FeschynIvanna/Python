from models.pen import Pen


class RulerPen(Pen):

    def __init__(self, id, color, brand, size, num_ruler, ruler_type):
        """
        Initializes an instance of the RulerPen class with the given properties.
        :param id:The unique identifier of the pen set.
        :param color:The color of the pen set.
        :param brand:The brand of the pen set.
        :param size:The size of the pen set.
        :param num_ruler:The number of markers in the pen set.
        :param ruler_type:The type of the pen set.
        """
        super().__init__(id, color, brand, size)
        self.ruler_type = ruler_type
        self.price_ruler = 7
        self.num_ruler = num_ruler
        self.pattern = {"geometric shapes"}

    def calculate_price(self):
        """
        A method for calculating the price of a pencil case
        """
        return self.num_ruler * self.price_ruler

    def __str__(self):
        return f"RulerPen(id={self.id}, color={self.color}, brand={self.brand}," \
                   f" size={self.size}, num_ruler={self.num_ruler}, marker_type={self.ruler_type})"
