class Character:

    def __init__(self, name_, initiative_, endurance_, attack_, agility_):
        self.name = name_
        self.initiative = initiative_
        self.endurance = endurance_
        self.attack = attack_
        self.agility = agility_

    def __str__(self):
        return self.name + " " + self.initiative + ", " +  self.endurance + ", " +  self.attack + ", " +  self.agility