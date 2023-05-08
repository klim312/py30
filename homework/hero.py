class SuperHero:
    people = 'people'
    def __int__(self,name, nickname,superpower,health_points, catchphrase):
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
        return f"{self.nickname}, {self.superpower}, {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Bruce Wayne', 'Batman', 'Genius-level intellect and martial arts', 100, 'I am Batman')
hero.get_name()
hero.double_health_points()
print(hero)
print(len(hero))