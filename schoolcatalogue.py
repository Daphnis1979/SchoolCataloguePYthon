class School:
  def __init__(self, name, level, number):
    self.name = name
    self.level = level
    self.number= number

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_number(self):
    return self.number

  def set_number(self,newNumber):
    self.number= newNumber

  def __repr__(self):
    return "A " + str(self.level) + " school named " + self.name + " with " + str(self.number) + " students"

class Primary(School):
  def __init__(self, name, number, policy):
    super().__init__(self, 'primary', number) 
    self.policy = policy

  def get_policy(self):
    return self.policy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {policy}".format(policy=self.policy)

b = Primary("Oxford", 400, "Pickup Allowed")
print(b.get_policy())

class HighSchool(School):
  def __init__(self, name, numberOfStudent, sportsTeams):
    super().__init__(name, 'High', numberOfStudent)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    parent = super().__repr__()
    return parent + f" information of our sport Team {self.sportsTeams}"

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c)
