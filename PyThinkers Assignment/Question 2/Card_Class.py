from dataclasses import dataclass

@dataclass
class Card:
    __rank:str = ''
    __suit:str = ''

    def getCard(self):
        return f"{self.__rank} of {self.__suit}"