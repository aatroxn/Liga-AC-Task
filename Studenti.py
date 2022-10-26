class person:
  def __init__(self, name, lname, age):
    self.firstname = name
    self.lastname = lname
    self.age = age

class student(person):
  def __init__(self, grade, university):
    self.grade = grade # 0 - 10
    self.university = university
  def newgrade(grade):
    self.newgrade = grade


p1 = person("Walter","White", 19)
p2 = student(7.53 ,"Random University")
p2.newgrade(9.33)

print(p1.firstname)
print(p1.lastname)
print(p1.age)
print(p2.grade)
print(p2.university)