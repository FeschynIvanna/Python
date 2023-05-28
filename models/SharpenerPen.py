from models.Pen import Pen


class SharpenerPen(Pen):

    def __init__(self, id, color, brand, size, num_sharpener, sharpener_type):
        super().__init__(id, color, brand, size)
        self.sharpener_type = sharpener_type
        self.price_sharpener = 2
        self.num_sharpener = num_sharpener

    def calculate_price(self):
        return self.num_sharpener * self.price_sharpener

    def __str__(self):
        return f"SharpenerPen(id={self.id}, color={self.color}, brand={self.brand}," \
                   f" size={self.size}, num_sharpener={self.num_sharpener}, sharpener_type={self.sharpener_type})"
