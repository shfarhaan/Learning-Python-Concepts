class Pokemon:
  def __init__(self, name, level, type, max_health, hitpoints, current_health, knocker_out):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level
    self.hitpoints = hitpoints
    self.current_health = self.max_health
    self.knocked_out = knocked_out

  def __pokedex__(self):
    return f"The Pokemon is {self.name}. It is a {self.type} Pokemon. It seems it's current level is {self.level} and a total hitpoints of {self.hitpoints}"
  def lose_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      self.is_knocked_out()

  def gain_health(self, heal):
    self.health += heal
    print(f"{self.name} has gained {heal} hitpoints and {self.name}'s health: {self.health}. Take {self.name} to the nearest Pokecenter or feed some berries!")

    def is_knocked_out(self):
      if self.knocked_out:
        print(f"{self.name} is already knocked out! Take {self.name} to the nearest Pokecenter.")
      else:
        self.knocked_out = True
        print(f"{self.name} has been knocked out! Take {self.name} to the nearest Pokecenter.")

    def revive(self):
      if self.knocked_out:
        self.knocked_out = False
        self.health = 1
        print(f"{self.name} has been revived with {self.health} health!")
      else:
        print(f"{self.name} is knocked out! Take {self.name} to the nearest Pokecenter.")

    def attack(self,other, damage):



