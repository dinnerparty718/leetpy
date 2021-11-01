
# self is similar to 'this' in java
class Robot:  # singular

    def introduce_self(self):
        print(f'hello my name is {self.name}')

    def __init__(self, color, weight=180, name='default Name') -> None:
        self.name = name
        self.color = color
        self.weight = weight

    @classmethod
    def speak(cls):
        print('robot is speaking')


class Person:
    # Class Object Attribute
    # value does not change
    # Person.membership
    membership = True

    def __init__(self, name, personality, isSitting) -> None:
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False


def main():
    r1 = Robot('YY', 'red', 30)
    r2 = Robot('ZZ', 'yellow', 30)

    p1 = Person('Alice', 'aggressive', False)
    p2 = Person('Becky', 'talkative', True)

    p1.robot_owned = r2
    p2.robot_owned = r1

    print(Person.membership)

    print(p1.robot_owned.introduce_self())

    r3 = Robot('red')
    print(r3.name, r3.color, end=" ")
    print('haha')

    Robot.speak()


if __name__ == '__main__':
    main()
