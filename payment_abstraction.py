from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def transaction(self):
        pass
class credit_card(payment):
    def transaction(self):
        print("payment done by credit card")
    def payment_status(self):
        print("done")
obj=credit_card()
obj.transaction()
obj.payment_status()
