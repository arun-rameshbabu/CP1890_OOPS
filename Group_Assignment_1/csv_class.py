from dataclasses import dataclass

@dataclass
class Customer:
    custid:int
    firstName:str
    lastName:str
    company:str
    address:str
    city:str
    state:str
    zipCode:str

    def custNameAddress(self):
        fullAddress = f"{self.state}" + ", " + f"{self.city}" + ", " + f"{self.address}" + ", " + f"{self.zipCode}"
        fullName = f"{self.firstName}" + " " + f"{self.lastName}"
        if self.company == "":
            return f"{fullName}\n{fullAddress}."
        else:
            return f"{fullName}\n{fullAddress}\n{self.company}."
