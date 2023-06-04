from decorator.pen_decorator import log_arguments_to_file, log_exceptions_to_file
from manager.pen_manager import PenManager
from models.school_pen import SchoolPen
from models.marker_pen import MarkerPen
from models.ruler_pen import RulerPen
from models.sharpener_pen import SharpenerPen

pens = [SchoolPen(101, "Green", "School", 14, 5, 6, 3),
        MarkerPen(101, "Yellow", "Tropic", 18, 6, "Technical"),
        RulerPen(101, "Red", "Schoolboy", 13, 5, "Plastic"),
        SharpenerPen(101, "Blue", "1September", 19, 7, "Plastic")]

for pen in pens:
    print(pen)

pen_manager = PenManager()

pen_manager.add_pens(pens)
pen_manager.add_pen(MarkerPen(101, "Pink", "Class", 17, 8, "Water"))

print()
print(pen_manager.find_all_the_bigger_than(15))
print()
pen_manager.find_by_color("Red")

print("\nList of size:")
print(pen_manager.list_of_size())

print("\nIndexed list:")
pen_manager.indexed_list()

print("\nNumeric list:")
pen_manager.numeric_list()

print("\nAll and Any conditions:")
print(pen_manager.check_condition_all_any(5))
