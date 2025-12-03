'''
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, p):
        distance = ((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2) ** 0.5
        return distance

class Segment3D:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        length = self.p1.distance_to(self.p2)
        return length

    def middle(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        z = (self.p1.z + self.p2.z) / 2
        p = Point3D(x,y,z)
        return p

    def cos_to(self, s):
        vector1 = (self.p2.x - self.p1.x, self.p2.y - self.p1.y, self.p2.z - self.p1.z)
        vector2 = (s.p2.x - s.p1.x, s.p2.y - s.p1.y, s.p2.z - s.p1.z)
        prod = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
        cos = prod / (self.length() * s.length())
        if cos < 0:
            cos = (- 1) * cos
        return cos



s1 = Segment3D(Point3D(0, 0, 0), Point3D(1, 2, 3))
s2 = Segment3D(Point3D(0, 0, 0), Point3D(1, 0, 0))

print(s1.cos_to(s2))
'''

class Creature:
    health_points: int

class EarthCreature(Creature):
    pass

class Troll(EarthCreature):
    health_points = 100

class Elf(EarthCreature):
    health_points = 80

class SeaCreature(Creature):
    pass

class Mermaid(SeaCreature):
    health_points = 60

class Siren(SeaCreature):
    health_points = 75

class AirCreature(Creature):
    pass

class Dragon(AirCreature):
    health_points = 120

class Pegasus(AirCreature):
    health_points = 85

class Player:
    id: int
    name: str
    scores: int
    games: list
    def __init__(self, id: int, name: str) -> None:
        self.id: int = id
        self.name: str = name
        self.scores: int = 0
        self.games: list = []

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        return self.scores / len(self.games)


class Player:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.scores = 0


class Power:

    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def use(self, player) -> None:
        raise NotImplementedError


class PhysicalPower(Power):

    def __init__(self, name: str, cost: int, count: int):
        self.name = name
        self.cost = cost
        self.count = count

    def use(self, player) -> None:
        if self.count > 0:
            print(f"{player.name} used {self.name}")
            self.count -= 1
        else:
            print(f"{player.name} cannot use {self.name}")


class MagicPower(Power):
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def use(self, player) -> None:
        print(f"{player.name} used {self.name}")
        player.scores += 1


class MagicPower(Power):
    name: str
    cost: int

    def __init__(self, name: str, cost: int) -> None:
        super().__init__(name, cost)

    def use(self, player: Player) -> None:
        print(f'{player.name} used {self.name}')
        player.scores += 1

p = Player(1, 'Bilbo')
t = PhysicalPower('teleport', 10, count=1)


print(p.scores)

b = MagicPower('black magic', 200)
b.use(p)
print(p.scores)
b.use(p)
print(p.scores)