from datetime import datetime, date, timedelta
class Invoice:
    def __init__(self,invoice_date):
        self.date=invoice_date


    def getDate(self):
        date_object = datetime.strptime(self.date,'%m/%d/%y')
        return date_object

    @property
    def getDueDate(self):
        return self.getDate() + timedelta(days=30)

def Datetoday():
    today = date.today()
    return today

def Overdue(Item):
    days = Datetoday() - Item.getDueDate
    if days < 0:
        print('This invoice is not yet due')
    elif days == 0:
        print('This invoice is due today')
    elif days > 0 :
        print(f'This invoice is {days} day(s) overdue.')

def title():
    print('The Invoice Due Date Program')
def main():
    title()
    invoiceDate = input('Enter the Invoice date (MM/DD/YY): ')
    Item = Invoice(invoiceDate)
    print()
    print(f"{'Invoice Date':20}: {Item.getDate():%B %d, %Y}")
    print(f"{'Due Date':20}: {Item.getDueDate:%B %d, %Y }")
    print(f"{'Current Date':20}: {Datetoday():%B %d, %Y }")
    print()
    Overdue(Item)


if __name__ == '__main__':
    main()