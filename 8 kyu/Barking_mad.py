# Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

# snoopy.bark() #return "Woof"
# scoobydoo.bark() #undefined
# Use method prototypes to enable all Dogs to bark.

# https://www.codewars.com/kata/54dba07f03e88a4cec000caf

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    self.bark = lambda: "Woof"
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")