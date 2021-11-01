class User():

    def __init__(self, email) -> None:
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email) -> None:
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows) -> None:
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        super().attack()
        print(f'attacking with arrows  of {self.num_arrows}')

# multiple inheritance


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows, email) -> None:
        # super().__init__(name, power, email)
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power, email)


wizard1 = Wizard('Merlin', 50, 'inin19@me.com')
archer1 = Wizard('Robin', 100, 'inin19@me.com')
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(1, object))

# polymorphysm
for char in [wizard1, archer1]:
    char.attack()


print(wizard1.email)


# introspection
# determine type of object at runtime
# print(dir(wizard1))


class Toy():
    def __init__(self, color, age) -> None:
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo'
        }

    def __str__(self) -> str:
        return f'{self.color}'

    def __call__(self, *args, **kwds) -> None:
        print('Yes')


action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(action_figure)
action_figure()


hb1 = HybridBorg('u', 30, 3, 'ii')
# hb1.attack()
