class Person:
  'Person base class'
  want_to_hack = True
  
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def printName(self):
    print("My name is {}".format(self.name))

  def printAge(self):
    print("My age is {}".format(self.age))

bob = Person("bob",30)
alice = Person("alice", 44)
mallory = Person("Mallory", 55)

print(bob)
print(alice)
print(mallory)

print(bob.age)

print(hasattr(bob, "age"))

print(hasattr(bob, "agdfgee"))

print(getattr(bob, "age"))

setattr(bob,"cash",111.55)

print(getattr(bob, "cash"))

#delattr
print(bob.printName())
print(bob.printAge())

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
