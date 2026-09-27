from abc import ABC,abstractmethod
class notification(ABC):
    @abstractmethod
    def whatsapp(self):
        pass
    def twitter(self):
        pass
    def instagram(self):
        pass
class Phone(notification):
    def whatsapp(self):
        print("Got a whatsapp msg")
    def twitter(self):
        print("Got a twitter tweat")
    def instagram(self):
        print("Got an instagram notification")
class laptop(notification):
    def whatsapp(self):
        print("Check your messages")
    def twitter(self):
        print("You have got tweets")
    def instagram(self):
        print("You have got messages")

