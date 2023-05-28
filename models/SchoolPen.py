from models.Pen import Pen


class SchoolPen(Pen):
    def __init__(self, id, color, brand, size, num_pencils, num_pens, num_erasers):
        super().__init__(id, color, brand, size)
        self.price_erasers = 2
        self.price_pen = 5
        self.price_pencils = 3
        self.num_erasers = num_erasers
        self.num_pens = num_pens
        self.num_pencils = num_pencils

    def calculate_price(self):
        return self.num_pencils * self.price_pencils + self.num_pens * self.price_pen + self.num_erasers * self.price_erasers

    def __str__(self):
        return f"SchoolPen(id={self.id}, color={self.color}, brand={self.brand}," \
               f" size={self.size}, num_pencils={self.num_pencils}, num_pens={self.num_pens}, num_erasers={self.num_erasers})"
