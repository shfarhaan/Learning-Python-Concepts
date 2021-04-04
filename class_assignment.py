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
        
        def gain_exp(self, exp):
    self.exp += exp
    print("{} gained {} xp.\n".format(self.name, exp))
    if self.exp >= 3:
      self.level_up()
  
  def level_up(self):
    self.exp = 0
    self.level += 1
    self.max_health += 1
    self.health = self.max_health
    print("{} leveled up to level {}! Max health now is {}. Health fully regenerated.\n".format(self.name, self.level, self.max_health))
 


class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon
  
  def __repr__(self):
    return "Trainer info. {name}, has pokemons: {pokemons}, has {potions} potions, current pokemon is {current_pokemon}.".format(name = self.name, pokemons = self.pokemons, potions = self.potions, current_pokemon = self.current_pokemon)
  
  def use_potion(self):
    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
        self.current_pokemon.gain_health(1)
        self.potions -= 1
        print("{} has {} potions left.\n".format(self.name, self.potions))
      else:
        print("{} failed to use a potion on {}. Your pokemon has maximum health.\n".format(self.name, self.current_pokemon.name))
    else:
      print("{}, you have no potions!\n".format(self.name))
  
  def attack(self, other, dmg):
    self.current_pokemon.attack(other.current_pokemon, dmg)
  
  def switch_pokemon(self, pokemon):
    if pokemon.is_knocked_out == True:
      print("You can't switch to a knocked out pokemon!")
    elif pokemon in self.pokemons:
      self.current_pokemon = pokemon
      print("{} switched a pokemon. {}'s current pokemon now is {}.\n".format(self.name, self.name, self.current_pokemon.name))



class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out):
    super().__init__(name, level, type, is_knocked_out)
  
  def destroy(self, other):
    other.lose_health(other.health)
    print("{} totally destroyed {}!".format(self.name, other.name))
        
