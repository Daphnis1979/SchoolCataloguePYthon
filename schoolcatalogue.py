class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level
  
  def getNumberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self, newNumber):
    self.numberOfStudents = newNumber 
    
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

a = School("Your Mom", "High", 300)
print(a)
print(a.getName())
print(a.getLevel())
print(a.getNumberOfStudents())
a.setNumberOfStudents(350)
print(a)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)


b = PrimarySchool("YourMom2", 450, "Pickup Allowed")
print(b)
print(b.getName())
print(b.getLevel())
print(b.getNumberOfStudents())
b.setNumberOfStudents(300)
print(b.getNumberOfStudents())
print(b.getPickupPolicy())
print(b)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "This school features the following sports teams: {sportsTeams}".format(sportsTeams = self.sportsTeams)

c = HighSchool("YourMom3", 548020, ["Syncronized Macrame", "FratBoy Date Rape"])
print(c)
print(c.getName())
print(c.getLevel())
print(c.getNumberOfStudents())
c.setNumberOfStudents(300)
print(c.getNumberOfStudents())
print(c.getSportsTeams())
print(c)
