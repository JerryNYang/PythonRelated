# jerry D Inyang
# backbone ...
class Employees:

	def __init__(self, name, department, role, salary, years_employed):
		self.name = name
		self.department = department
		self.role = role
		self.salary = salary
		self.years_employed = years_employed
		
	def eligible_for_retirement(self):
		if self.years_employed >= 235:
			return True
		else:
			return False


