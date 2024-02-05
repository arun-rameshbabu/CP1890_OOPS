from datetime import datetime, date, timedelta
from dataclasses import dataclass


@dataclass
class Invoice:
    date: str

    def getDate(self):
        date_object = datetime.strptime(self.date, '%m/%d/%y')
        return date_object

    @property
    def getDueDate(self):
        dueDays = self.getDate() + timedelta(days=30)
        return dueDays


def Datetoday():
    today = datetime.now()
    return today


def Overdue(Item):
    days = Datetoday() - Item.getDueDate
    if days.days < 0:
        print('This invoice is not yet due')
    elif days.days == 0:
        print('This invoice is due today')
    elif days.days > 0:
        print(f'This invoice is {days.days} day(s) overdue.')


def title():
    print('The Invoice Due Date Program')


def main():
    title()
    cont = 'y'
    while cont.lower() == 'y':
        invoiceDate = input('Enter the Invoice date (MM/DD/YY): ')
        Item = Invoice(invoiceDate)
        print()
        print(f"{'Invoice Date':20}: {Item.getDate():%B %d, %Y}")
        print(f"{'Due Date':20}: {Item.getDueDate:%B %d, %Y }")
        print(f"{'Current Date':20}: {Datetoday():%B %d, %Y }")
        print()
        Overdue(Item)
        print()
        cont = input('Continue? (y/n): ')


if __name__ == '__main__':
    main()