
class Cordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

oringin = Cordinate(0,0)
c = Cordinate(3,4)
print(c.x)


# Spell methods

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())


#### CLAS A CLAS B

