from manager.PenManager import PenManager
from models.SchoolPen import SchoolPen
from models.MarkerPen import MarkerPen
from models.RulerPen import RulerPen
from models.SharpenerPen import SharpenerPen


pens = [SchoolPen(101, "Green", "School", 14, 5, 6, 3),
        MarkerPen(101, "Yellow", "Tropic", 18, 6, "Technical"),
        RulerPen(101, "Red", "Schoolboy", 13, 5, "Plastic"),
        SharpenerPen(101, "Blue", "1September", 19, 7, "Plastic")]

for pen in pens:
    print(pen)

pen_manager = PenManager()

pen_manager.add_pens(pens)
pen_manager.add_pen(MarkerPen(101, "Pink", "Class", 17, 8, "Water"))

print("\n")
pen_manager.find_all_the_bigger_than(15)
print("\n")
pen_manager.find_by_color("Red")

