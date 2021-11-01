'''
encapsulation
    Encapsulation can be viewed as a shield that protects data from getting accessed by outside code. 
    In essence, Encapsulation binds data and code as a single unit and enforces modularity. 




abstraction
    detail of implementation of hidden away from the user
    only essentail things are displayed to the user

    abstract away things user does not need to know
    user do not care about implementation
    just need to access it and use it
    protecting using private variables, only convention
        _name
        _age
        shouldn't be modified, no garantee

inheritance
    abstract away things that are shared
    changing things according to what each one need

    Inheritance ensures that codes are reused
    A parent class can share its attributes with a child class

    to check isinstance

polymorphism
    many forms
    subclasses can share method name but have different implementation base on Attribute

    issubclass(list, object)

'''


# self is similar to 'this' in java
class Robot:  # singular

    def introduce_self(self):
        print(f'hello my name is {self.name}')

    def __init__(self, color, weight=180, name='default Name') -> None:
        self._name = name
        self._color = color
        self._weight = weight

    @classmethod
    def duplicate(cls):
        print('robot is duplicating')
        return cls('yellow')

    @staticmethod  # no access to cls
    def myStatic():
        pass


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

    r4 = Robot.duplicate()

    print(r4)


if __name__ == '__main__':
    main()
