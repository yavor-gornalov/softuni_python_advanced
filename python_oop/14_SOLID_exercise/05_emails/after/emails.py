from abc import ABC, abstractmethod


class IProtocol(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class IMProtocol(IProtocol):
    def format(self):
        return f"I'm {self.name}"


class NameProtocol(IProtocol):
    def format(self):
        return f"My name is {self.name}"


class MyMl(IContent):
    def format(self):
        return f"<myML>\n{self.text}\n</myML>"


class HTML(IContent):
    def format(self):
        return f"<html>\n{self.text}\n</html>"


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IProtocol):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IProtocol):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myml = MyMl('Hello, there!')
sender_name = NameProtocol('qmal')
receiver_name = NameProtocol('james')
email = Email()
email.set_sender(sender_name)
email.set_receiver(receiver_name)
email.set_content(myml)
print(email)
