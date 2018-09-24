class baseCharacter:

    charstats = {}
    token = None
    speed = None
    health = None
    defence = None
    charlocation = None
    charname = None
    player = None

    def __str__(self):
        printout = "Player{}'s name is {}, character token is {} and character " \
                   'location is {}.'.format(self.player, self.charname, self.token, self.charlocation)
        return printout

    def __repr__(self):
        return self.__str__()


