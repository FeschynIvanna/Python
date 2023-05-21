from models.Pen import Pen


class MarkerPen(Pen):
    def __init__(self, id, color, brand, size, num_marker, marker_type):
        super().__init__(id, color, brand, size)
        self.marker_type = marker_type
        self.price_marker = 5
        self.num_marker = num_marker

    def calculate_price(self):
        return self.num_marker * self.price_marker

    def __str__(self):
        return f"MarkerPen(id={self.id}, color={self.color}, brand={self.brand}," \
               f" size={self.size}, num_marker={self.num_marker}, marker_type={self.marker_type})"
