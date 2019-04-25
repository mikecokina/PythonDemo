from dataclasses import dataclass, field
from typing import List


print("\nbasic ---------------------------------------")
@dataclass
class Person:
    firstname: str
    lastname: str


person = Person('Foo', 'Bar')
print(person.firstname)
person.firstname = 'Fooooo'
print(person.firstname)
print(person == Person('Fooooo', 'Bar'))
print("\n/basic --------------------------------------")


print("\ndefault -------------------------------------")
# defaults
@dataclass
class Position:
    name: str
    x: float = 0.0
    y: float = 0.0


pos = Position('first')
print(pos)
pos = Position('second', 1.0, 2.0)
print(pos)
print("\n/default ------------------------------------")


print("\ntyping --------------------------------------")
@dataclass
class Attendee:
    firstname: str
    lastname: str


def default_attendee() -> List[Attendee]:
    return [Attendee('Foo', 'Bar'), Attendee('Baar', 'Fooo')]


@dataclass
class Conference:
    name: str
    location: str
    attendees: List[Attendee] = field(default_factory=default_attendee)

    @property
    def conf_repr(self):
        return f'{self.name} in {self.location}'


conf = Conference('PyCon', 'BA')
print(conf.attendees)
print(type(conf.attendees))
print(conf.conf_repr)
print("\n/typing -------------------------------------")