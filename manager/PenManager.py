class PenManager:
    def __init__(self):
        self.pens = []

    def add_pen(self, new_pen):
        self.pens.append(new_pen)

    def add_pens(self, pens):
        self.pens.extend(pens)

    def find_all_the_bigger_than(self, size):
        print("Pens the biggest: ")
        for pen in self.pens:
            if pen.size > size:
                print(pen)

    def find_by_color(self, color):
        print("Pens with this color: ")
        for pen in self.pens:
            if pen.color == color:
                print(pen)
