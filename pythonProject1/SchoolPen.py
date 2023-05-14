class SchoolPen:

    def __init__(self, id=101, brand=" ", color=" ", material=" ", size=0, num_pencils=0, num_pens=0, num_erasers=0):
        self.__id = id
        self.__brand = brand
        self.__color = color
        self.__material = material
        self.__size = size
        self.__num_pencils = num_pencils
        self.__num_pens = num_pens
        self.__num_erasers = num_erasers

    @property
    def id(self):
        return self.__id

    @property
    def brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @property
    def material(self):
        return self.__material

    @property
    def size(self):
        return self.__size

    @property
    def num_pencils(self):
        return self.__num_pencils

    @property
    def num_pens(self):
        return self.__num_pens

    @property
    def num_erasers(self):
        return self.__num_erasers

    @id.setter
    def id(self, id):
        self.__id = id

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @color.setter
    def color(self, color):
        self.__color = color

    @material.setter
    def material(self, material):
        self.__material = material

    @size.setter
    def size(self, size):
        self.__size = size

    @num_pencils.setter
    def num_pencils(self, num_pencils):
        self.__num_pencils = num_pencils

    @num_pens.setter
    def num_pens(self, num_pens):
        self.__num_pens = num_pens

    @num_erasers.setter
    def num_erasers(self, num_erasers):
        self.__num_erasers = num_erasers

    def add_pencil(self):
        if self.__num_pencils < self.size:
            self.__num_pencils += 1

    def add_pen(self):
        if self.__num_pens < self.size:
            self.__num_pens += 1

    def remove_pencil(self):
        if self.__num_pencils > 0:
            self.__num_pencils -= 1

    def remove_pen(self):
        if self.__num_pens > 0:
            self.__num_pens -= 1

    def __str__(self):
        return f"SchoolPen(id={self.__id}, brand={self.__brand}, color={self.__color}, material={self.__material}," \
               f"size={self.__size}, num_pencils={self.__num_pencils}, num_pens={self.__num_pens}," \
               f" num_erasers={self.__num_erasers})"

    @staticmethod
    def get_instance():
        SchoolPen.instance = SchoolPen()
        return SchoolPen.instance


school_pen1 = SchoolPen()
school_pen2 = SchoolPen(101, "September", "red", "cotton", 20, 7, 3, 2)
school_pens = [school_pen1, school_pen2, SchoolPen.get_instance(), SchoolPen.get_instance()]

for school_pen in school_pens:
    print(school_pen)
