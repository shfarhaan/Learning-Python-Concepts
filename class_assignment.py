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
    
