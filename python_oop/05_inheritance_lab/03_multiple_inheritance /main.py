from project.person import Person
from project.employee import Employee
from project.teacher import Teacher

p = Person()
print(p.sleep())

e = Employee()
print(e.get_fired())

t = Teacher()
print(t.sleep(), t.get_fired(), t.teach())
