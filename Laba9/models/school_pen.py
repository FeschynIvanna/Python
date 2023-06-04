from models.pen import Pen


class SchoolPen(Pen):

    def __init__(self, id, color, brand, size, num_pencils, num_pens, num_erasers):
        """
        Initializes an instance of the SchoolPen class with the given properties.
        :param id:The unique identifier of the pen set.
        :param color:The color of the pen set.
        :param brand:The brand of the pen set.
        :param size:The size of the pen set.
        :param num_pencils:The number of pencils in the pen set.
        :param num_pens:The number of pens in the pen set.
        :param num_erasers: The number of erasers in the pen set.
        """
        super().__init__(id, color, brand, size)
        self.price_erasers = 2
        self.price_pen = 5
        self.price_pencils = 3
        self.num_erasers = num_erasers
        self.num_pens = num_pens
        self.num_pencils = num_pencils
        self.pattern = {"inscription from letters"}

    def calculate_price(self):
        """
        A method for calculating the price of a pencil case
        """
        return self.num_pencils * self.price_pencils + self.num_pens * self.price_pen + self.num_erasers * self.price_erasers

    def __str__(self):

        return f"SchoolPen(id={self.id}, color={self.color}, brand={self.brand}," \
               f" size={self.size}, num_pencils={self.num_pencils}, num_pens={self.num_pens}, num_erasers={self.num_erasers})"