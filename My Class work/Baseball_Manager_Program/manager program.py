from manager_program_objects import player
from datetime import datetime
def title ():
     print('='*100)
     print('Baseball Team Manager'.center(100))

# def Dates ():
#         d1 = datetime.datetime.now()
#
#         d1 = datetime.strptime(d1, "%Y-%m-%d")
#         print('CURRENT DATE: ',di)
#         d2 = input('GAME DATE: ')
#         d2 = datetime.strptime(d2, "%Y-%m-%d")
#         print(abs((d2 - d1).days))

def menu():
    print('MENU OPTIONS'+
          '\n1 - Display lineup'+
          '\n2 - Add player'+
          '\n3 - Remove)