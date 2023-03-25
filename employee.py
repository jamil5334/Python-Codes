#python code to print employee details and compute overtime
class Employee(object):
	"""docstring for Employee"""
	def __init__(self, emp_id, emp_name, emp_salary, emp_department):
		self.emp_id = emp_id
		self.emp_name= emp_name
		self.emp_salary= emp_salary
		self.emp_department= emp_department

	def employee_details(self):
		print("Employee ID:", self.emp_id)
		print("Employee Name:", self.emp_name)
		print("Employee Salary:", self.emp_salary)
		print("Employee Department:", self.emp_department)

	def calculate_emp_salary(self, hours_worked):
		if hours_worked>50:
			overtime_hours= hours_worked-50
			overtime_amount= overtime_hours*(self.emp_salary/50)
			total_pay= self.emp_salary+overtime_amount
			return total_pay
		else:
			return self.emp_salary

emp= Employee("KU27", "Joy", 65000, "Tourism")
sal=Employee.calculate_emp_salary(60)
print("Employee's total pay:", salary)
Employee.employee_details()
