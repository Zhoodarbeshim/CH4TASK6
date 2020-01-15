class House():
    def __init__(self, Houshold_type, total_area):
        self.Houshold_type = Houshold_type
        self.total_area = total_area
        print(self.Houshold_type, self.total_area)

    def furniture(self, bed, wardrobe, table):
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table
        self.bed_area = 4
        self.wardrobe_area = 2
        self.table_area = 1.5
        print(f"{self.bed}: {self.bed_area} m2, {self.wardrobe}: {self.wardrobe_area} m2, {self.table}: {self.table_area} m2")

obj1 = House("private house", 100)
obj1.furniture("bed", "wardrobe", "table")