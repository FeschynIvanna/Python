from models.Pen import Pen


class RulerPen(Pen):

    def __init__(self, id, color, brand, size, num_ruler, ruler_type):
        super().__init__(id, color, brand, size)
        self.ruler_type = ruler_type
        self.price_ruler = 7
        self.num_ruler = num_ruler

    def calculate_price(self):
        return self.num_ruler * self.price_ruler

    def __str__(self):
        return f"RulerPen(id={self.id}, color={self.color}, brand={self.brand}," \
                   f" size={self.size}, num_ruler={self.num_ruler}, marker_type={self.ruler_type})"
