
# Базовый класс персонажа, используется, как для мобов так и для чуваков игрока

class Creature(object):
    def __init__(self, key):
        self.key = key
        # Базовые статы
        self.strength = float()
        self.dexterity = float()
        self.endurance = float()
        self.speed = float()
        self.technic= float()
        self.resphys = float()
        self.resthermo = float()
        self.reschem = float()
        self.dodge = float()

    def get_key(self):
        print(self.key)