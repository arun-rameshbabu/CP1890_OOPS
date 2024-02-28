from dataclasses import dataclass
from datetime import datetime

@dataclass
class Days:
    date:str = "d/m/y"

    def getDate(self):
        return datetime.strptime(self.date, "%d/%m/%Y").date()

    def getDay(self):
        date = str(self.getDate).split(',')
        date2 = date[0].removesuffix("s")
        return date2
