from models.pen import Pen


class MarkerPen(Pen):
    def __init__(self, id, color, brand, size, num_marker, marker_type):
        """
        Initializes an instance of the MarkerPen class with the given properties.
        :param id:The unique identifier of the pen set.
        :param color:The color of the pen set.
        :param brand:The brand of the pen set.
        :param size:The size of the pen set.
        :param num_marker:The number of markers in the pen set.
        :param marker_type:The type of the pen set.
        """
        super().__init__(id, color, brand, size)
        self.marker_type = marker_type
        self.price_marker = 5
        self.num_marker = num_marker
        self.pattern = {"the hero from the cartoon"}

    def calculate_price(self):
        """
        A method for calculating the price of a pencil case
        """
        return self.num_marker * self.price_marker

    def __str__(self):
        return f"MarkerPen(id={self.id}, color={self.color}, brand={self.brand}," \
               f" size={self.size}, num_marker={self.num_marker}, marker_type={self.marker_type})"

    def __repr__(self):
        return f"MarkerPen(id={self.id}, color={self.color}, brand={self.brand}," \
               f" size={self.size}, num_marker={self.num_marker}, marker_type={self.marker_type})"