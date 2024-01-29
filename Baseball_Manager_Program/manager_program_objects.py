from dataclasses import dataclass

@dataclass


class player:
    __firstName: str
    __lastName: str
    __position: str
    __atBats: int = 0
    __hits: int = 0


    def __post_init__(self):

        self.__firstName = self.firstName

        self.__lastName = self.lastName

        self.__position = self.position

        self.__atBats =  self.atBats

        self.__hits = self.hits
    @player_setter
    def setFirsName(self, firstName):
        self.__firstName = firstName
    def setFirsName(self, lastName):
        self.__lastName = lastName
    def setFirsName(self, position):
        self.__position= position
    def setFirsName(self, atBats):
        self.__atBats = atBats
    def setFirsName(self, hits):
        self.__hits = hits


    @property
    def getFullName(self) -> str:
        return f"{self.__firstName} {self.__lastName}"

    def getAverage(self):
        return self.__hits/self.__atBats



    def players(self):
        return self.__players


        print(f"  {'Player:25'} {'POS':4} {'AB':>5} {'H':>5} {'AVG':>5}")
        for i, player in enumerate(players_list, start = 1 ):
            print("{}. {:25} {:>4} {:>5.d} {:>5.d} {:>5.3f} ".format(i, player.getFullName(), player.getPosition(),player.getAtBats(),player.getHits(),player.getAverage()))



