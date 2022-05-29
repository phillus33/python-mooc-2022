# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.{self.__cents:02} eur"
        return f"{self.__euros}.{self.__cents} eur"

    def __eq__(self, another: 'Money'):
        return self.__to_cents() == another.__to_cents()

    def __lt__(self, another: 'Money'):
        return self.__to_cents() < another.__to_cents()

    def __gt__(self, another: "Money"):
        return self.__to_cents() > another.__to_cents()

    def __ne__(self, another: "Money"):
        return self.__to_cents() != another.__to_cents()

    def __to_cents(self):
        return self.__euros * 100 + self.__cents

    def __to_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100

    def __add__(self, another: "Money"):
        # this is smooth brain solution
        # new_euros = self.__euros + another.__euros
        # new_cents = self.__cents + another.__cents
        # if new_cents > 99:
        #     new_euros += 1
        #     new_cents -= 100
        # return Money(new_euros, new_cents)

        # this is big brain solution with helper methods
        new_money = Money(0,0)
        new_money.__to_value(self.__to_cents() + another.__to_cents())
        return new_money

    def __sub__(self, another):
        # this is smooth brain solution
        # if another > self:
        #     raise ValueError("a negative result is not allowed")
        # new_euros = self.__euros - another.__euros
        # new_cents = self.__cents - another.__cents
        # if new_cents < 0:
        #     new_euros -= 1
        #     new_cents = 100 + new_cents
        # return Money(new_euros, new_cents)

        # this is big brain solution with helper methods
        difference = self.__to_cents() - another.__to_cents()
        if difference < 0:
            raise ValueError("a negative result is not allowed")

        new_money = Money(0,0)
        new_money.__to_value(self.__to_cents() - another.__to_cents())
        return new_money
        
