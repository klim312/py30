class SuperHero:
    people = 'people'

    def init(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)



    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Hero: Nickname {self.nickname}, Superpower {self.superpower}, health_points {self.health_points}'

    def __len__(self):
        return f'SuperHero("{self.name}", "{self.nickname}", "{self.superpower}", {self.health_points}, "{self.catchphrase}")'


hero = SuperHero
hero.print_name()
hero.double_health()
print(hero)
print(len(hero))
