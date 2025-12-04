from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def __init__(self, amount:int):
        self.amount = amount

    @abstractmethod
    def process(self, amount:int) ->None:
        pass


class Credit(PaymentMethod):
    def process(self) ->None:
        print(f"you have paid {self.amount} dollars with credit method")


class Crypto(PaymentMethod):
    def process(self) ->None:
        print(f"you have paid {self.amount} dollars with crypto method")

class Paypal(PaymentMethod):
    def process(self) ->None:
        print(f"you have paid {self.amount} dollars with paypal method")



# print(Credit(50).process())
# print(Crypto(50).process())
# print(Paypal(50).process())


class Payment:
    @staticmethod
    def processPayment(method: PaymentMethod) ->None:
        method.process()


def clientCode(method, amount: int) -> str:
    MethodToClass = {
        'crypto': Crypto,
        'paypal': Paypal,
        'credit': Credit,
    }
    paymentClass = MethodToClass[method]
    objectPaymentClass = paymentClass(amount)
    return Payment.processPayment(objectPaymentClass)




print(clientCode('crypto', 10))
print(clientCode('paypal', 20))
print(clientCode('credit', 50))
