
# self is similar to 'this' in java
class Robot:
    def introduce_self(self):
        print(f'hello my name is {self.name}')

    def __init__(self, name, color, weight) -> None:
        self.name = name
        self.color = color
        self.weight = weight


class Person:
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

    print(p1.robot_owned.introduce_self())


if __name__ == '__main__':
    main()
