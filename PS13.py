
class Employee:
  def __init__(self, first='N/A', last='N/A', pay=0.0, joblevel=1):
      self.first = first
      self.last = last
      self.pay = pay
      self.joblevel = joblevel

  def shortbonus(self):
      if self.joblevel == 1:
          return 0.25 * self.pay
      elif self.joblevel == 2:
          return 0.20 * self.pay
      elif self.joblevel == 3:
          return 0.10 * self.pay
      else:
          return 0

  def longbonus(self):
      return 0.10 * self.pay


empl1 = Employee('Eddie', 'Brock', 60000.00)
empl2 = Employee('Peter', 'Parker', 80000.00, joblevel=2)
empl3 = Employee('Wade', 'Wilson', 70000.00, joblevel=3)

print(empl1.first)
print(empl1.last)
print(empl1.pay)
print("Short term bonus:", empl1.shortbonus())
print("Long term bonus:", empl1.longbonus())

print(empl2.first)
print(empl2.last)
print(empl2.pay)
print("Short term bonus:", empl2.shortbonus())
print("Long term bonus:", empl2.longbonus())

print(empl3.first)
print(empl3.last)
print(empl3.pay)
print("Short term bonus:", empl3.shortbonus())
print("Long term bonus:", empl3.longbonus())

class Manager(Employee):
  def __init__(self, first='N/A', last='N/A', pay=0.0, joblevel=1, auto='N/A'):
      super().__init__(first, last, pay, joblevel)
      self.auto = auto

  def display_auto(self):
      return self.auto

  def longbonus(self):
      if self.joblevel == 1:
          return 0.50 * self.pay
      elif self.joblevel == 2:
          return 0.40 * self.pay
      elif self.joblevel == 3:
          return 0.35 * self.pay
      else:
          return 0


manager1 = Manager('Mary Jane', 'Watson', 60000.00, auto='Honda')
manager2 = Manager('Steve', 'Stevenson', 80000.00, joblevel=2, auto='BMW')
manager3 = Manager('Toad', 'Bridage', 70000.00, joblevel=3, auto='Audi')


print(manager1.first)
print(manager1.last)
print(manager1.pay)
print("Short term bonus:", manager1.shortbonus())
print("Long term bonus:", manager1.longbonus())
print("Automobile:", manager1.display_auto())

print(manager2.first)
print(manager2.last)
print(manager2.pay)
print("Short term bonus:", manager2.shortbonus())
print("Long term bonus:", manager2.longbonus())
print("Automobile:", manager2.display_auto())

print(manager3.first)
print(manager3.last)
print(manager3.pay)
print("Short term bonus:", manager3.shortbonus())
print("Long term bonus:", manager3.longbonus())
print("Automobile:", manager3.display_auto())
