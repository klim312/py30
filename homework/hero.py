class SuperHero:
    people = 'people'
    def __init__(self,name, nickname,superpower,health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
    def get_name(self):
        print(self.name)
    def double_health_points(self):
        self.health_points *= 2
    def __str__(self):
        return f"{self.nickname}    , {self.superpower}, {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Bruce Wayne', 'Batman', 'Genius-level intellect and martial arts', 100, 'I am Batman')
hero.get_name()
hero.double_health_points()
print(hero)
print(len(hero))


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_hp(self):
        self.health_points **= 2
        self.fly = True

    def fly_phrase(self):
        if self.fly:
            print('Fly in the True_phrase')


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_hp(self):
        self.health_points **= 2
        self.fly = True

class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2


air_hero = AirHero('Clark Kent', 'Superman', 'super strength and flight', 100, "Up, up, and away!", 10)
print(air_hero)
air_hero.double_hp()
air_hero.fly_phrase()

earth_hero = EarthHero('Bruce Wayne', 'Batman', 'intelligent and skilled fighter', 75, "I'm Batman.", 8)
print(earth_hero)
earth_hero.double_hp()
print(earth_hero)

villain = Villain('Peter Parker', 'Spiderman', 'dexterity and web', 150, 'I am Spiderman', 12)
print(villain)
villain.double_hp()
villain.fly_phrase()
print(villain.damage)
print(villain.crit())