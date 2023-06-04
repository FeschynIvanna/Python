from models.pen import Pen


class SharpenerPen(Pen):

    def __init__(self, id, color, brand, size, num_sharpener, sharpener_type):
        """
        Initializes an instance of the SharpenerPen class with the given properties.
        :param id:The unique identifier of the pen set.
        :param color:The color of the pen set.
        :param brand:The brand of the pen set.
        :param size:The size of the pen set.
        :param num_sharpener:The number of markers in the pen set.
        :param sharpener_type:The type of the pen set.
        """
        super().__init__(id, color, brand, size)
        self.sharpener_type = sharpener_type
        self.price_sharpener = 2
        self.num_sharpener = num_sharpener
        self.pattern = {"flowers"}

    def calculate_price(self):
        """
        A method for calculating the price of a pencil case
        """
        return self.num_sharpener * self.price_sharpener

    def __str__(self):
        return f"SharpenerPen(id={self.id}, color={self.color}, brand={self.brand}," \
                   f" size={self.size}, num_sharpener={self.num_sharpener}, sharpener_type={self.sharpener_type})"