class Pokemon:

    def __init__(self, name, level, type, max_health, hitpoints, current_health, knocker_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level
        self.hitpoints = hitpoints
        self.current_health = self.max_health
        self.knocker_out = knocker_out

    def __pokedex__(self):
        return f"The Pokemon is {self.name}. It is a {self.type} Pokemon. It seems it's current level is {self.level} and a total hitpoints of {self.hitpoints}"
    
    def lose_health(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        
    def gain_health(self, heal):
        self.health += heal
        print("{} gained {} health".format(self.name, heal))
        print("{}'s health: {}".format(self.name, self.health))
  
    def knock_out(self):
        if self.is_knocked_out:
            print("{name} is already knocked out.".format(name=self.name))
        else:
            self.is_knocked_out = True
            print("{name} is knocked out!".format(name=self.name))
    
    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.health = 1
            print("{name} has been revived with {health} health!".format(name=self.name, health=self.health))
        else:
            print("{name} is not knocked out.".format(name=self.name))
    
    def attack(self, other, dmg):
        if self.is_knocked_out == True:
            print("You can not attack. {pokemon} is knocked out!".format(pokemon=self.name))
            return
        if self.type == 'Water':
            if other.type == 'Fire':
                dmg *= 2
            elif other.type == 'Grass':
                dmg /= 2
        elif self.type == 'Fire':
            if other.type == 'Grass':
                dmg *= 2
            elif other.type == 'Water':
                dmg /= 2
        elif self.type == 'Grass':
            if other.type == 'Water':
                dmg *= 2
            elif other.type == 'Fire':
                dmg /= 2
        other.lose_health(dmg)
        print("{} attacked {}".format(self.name, other.name))
        print("{} dealt {} damage to {}. His health is {}.".format(self.name, dmg, other.name, other.health))
        
