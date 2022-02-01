from abc import ABC, abstractmethod

class PriceStrategy(ABC):

    @abstractmethod
    def compute_price(self, amount): pass

class DayDisscountPrice(PriceStrategy):

    __day = 4
    __disscount_percentage = 0.15

    def compute_price(self, amount):
        if self.__day == 5:
            return amount - amount * self.__disscount_percentage
        return amount

class CardPrice(PriceStrategy):
    __interest_percentage = 0.10

    def compute_price(self, amount):
        return amount + amount * self.__interest_percentage

class CashPrice(PriceStrategy):
    __disscount_percentage = 0.20

    def compute_price(self, amount):
        return amount - amount * self.__disscount_percentage

class ClientPrice(PriceStrategy):
    __disscount_percentage = 0.30

    def compute_price(self, amount):
        return amount - amount * self.__disscount_percentage

def set_strategy(option: int) -> PriceStrategy:
    strategies = {
        1: CardPrice(),
        2: CashPrice(),
        3: ClientPrice(),
        4: DayDisscountPrice()
    }
    return strategies[option]

if __name__ == '__main__':
    strategy = int(input("""Ingrese la estrategia de descuento
[1]Precio por pago con tarjeta
[2]Precio por pago en efectivo
[3]Precio por ser cliente
[4]Precio por dia de descuento
>>>: """))
    amount = int(input('Ingrese el monto total: $'))
    strategy = set_strategy(strategy)
    total = strategy.compute_price(amount)
    print(f'El total es: ${total}')