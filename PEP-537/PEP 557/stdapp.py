# named tuple
from collections import namedtuple

# tuple, dict, namedtuple
person = ('Foo', 'Bar')
print(person[0])  # lastname or surname???

person = {'firstname': 'Foo', 'lastname': 'Bar'}
print(person["firstname"])  # prefer dot notation???

Person = namedtuple('Person', ['firstname', 'lastname'])

person = Person(firstname='Foo', lastname='Bar')
print(person.firstname)
# person.firstname = 'Fooooo'


# class
class Person(object):
    def __init__(self, firstname, lastname, **kwargs):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, o):
        pass

    def __lt__(self, o):
        pass


person = Person('Foo', 'Bar')

print(person.firstname)
person.firstname = 'Foooooo'
print(person.firstname)
