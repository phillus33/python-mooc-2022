class Item:

    def __init__(self, name: str, weight: int):

        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase: 

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def __str__(self):

        ending = "s" if len(self.__items) != 1 else ""

        return f"{len(self.__items)} item{ending} ({self.weight()} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        curr_weight = 0
        for item in self.__items:
            curr_weight += item.weight()
        return curr_weight

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        
        heaviest_item = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest_item.weight():
                heaviest_item = item
        return heaviest_item


class CargoHold:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
            

    def weight(self):
        curr_weight = 0
        for item in self.__suitcases:
            curr_weight += item.weight()
        return curr_weight


    def __str__(self):
        optional_s = "s" if len(self.__suitcases) != 1 else ""
        return f"{len(self.__suitcases)} suitcase{optional_s}, space for {self.__max_weight - self.weight()} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()





if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()