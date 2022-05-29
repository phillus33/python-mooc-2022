class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __to_value(self):
        return self.__year * (12*30) + self.__month * 30 + self.__day

    def __to_date(self, days: int):
        year = days // 360
        month = (days // 30) % 12
        day = days % 30
        return SimpleDate(day, month, year)

    def __eq__(self, other: "SimpleDate"):
        return self.__to_value() == other.__to_value()

    def __ne__(self, other: "SimpleDate"):
        return self.__to_value() != other.__to_value()

    def __lt__(self, other: "SimpleDate"):
        return self.__to_value() < other.__to_value()
    
    def __gt__(self, other: "SimpleDate"):
        return self.__to_value() > other.__to_value()

    def __add__(self, days: int):
         return self.__to_date(self.__to_value() + days)

    def __sub__(self, other: "SimpleDate"):
        return abs(self.__to_value() - other.__to_value())


