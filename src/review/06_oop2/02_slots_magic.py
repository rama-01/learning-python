class Person(object):
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value


def main():
    person = Person('bruce', 12)
    print(person.name, person.age)
    person.name = 'johnson'
    person.age = 20
    print(person.name, person.age)
    person._gender = 'male'
    # person._hello = 'world'


if __name__ == '__main__':
    main()
