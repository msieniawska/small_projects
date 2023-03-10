# Based on https://github.com/pkienzle/periodictable
# pip install periodictable

import periodictable

atomic_number = int(input("Enter atomic number:"))
element = periodictable.elements[atomic_number]
print("Atomic number: ", element.number)
print("Symbol: ", element.symbol)
print("Name:", element.name)
print("Atomic mass:", element.mass)
print("Density:", element.density)
