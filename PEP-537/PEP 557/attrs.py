from dataclasses import dataclass


# frozen
@dataclass(frozen=True)
class Attendee:
    firstname: str
    lastname: str
    age: int


a = Attendee('Foo', 'Bar', 28)
print(a)


# a.age = 10

# order
@dataclass(order=True)
class Person:
    firstname: str
    lastname: str
    age: int


p = Person('foo', 'bar', 30)
print(p < Person('foo', 'bar', 50))


# inheritance
@dataclass
class User(Person):
    username: str


u = User('Foo', 'Bar', 30, 'user1')
print(u)
