from abc import ABC, abstractmethod

class Text(ABC):

    @abstractmethod
    def write(self): pass

class BaseText(Text):

    def write(self):
        print('some basic text')

class TextDecorator(Text):

    __decorated_text: Text

    def __init__(self, decorated_text):
        self.__decorated_text = decorated_text

    def write(self):
        self.__decorated_text.write()

class BoldTextDecorator(TextDecorator):

    def BoldTextDecorator(self, decorated_text: Text):
        return super().__decorated_text

    def write(self):
        print('adding bold style to text')
        return super().write()

class UnderlineTextDecorator(TextDecorator):

    def UnderlineTextDecorator(self, decorated_text: Text):
        return super().__decorated_text

    def write(self):
        print('adding underline style to text')
        return super().write()

base_text = BaseText()
base_text.write()

bold_text = BoldTextDecorator(base_text)
bold_text.write()

underline_text = UnderlineTextDecorator(base_text)
underline_text.write()
underline_text = UnderlineTextDecorator(bold_text)
underline_text.write()

