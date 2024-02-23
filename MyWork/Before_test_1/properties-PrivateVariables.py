class Ninja:
    def __init__(self):
        self.name = "Ninja"
        self._skill = 5
        self.__pid = 7754

    """
    def get_skill(self):
        return self._skill
    
    def set_skill(self, value):
        self._skill = value
    """

    @property
    def skill(self) -> int:
        return self._skill

    @skill.setter
    def skill(self, value):
        if value < 0:
            raise ValueError("No skills?")
        else:
            self._skill = value

    @skill.getter
    def skill(self):
        return self._skill + 50

n = Ninja()
print(n.name)
print(n._skill)
# print(n.__pid) <- cannot be accessed due to double underscore
print(dir(n))
print(n._Ninja__pid)

print(n.skill)
# n.skill = -50 # <- raises error as seen above
