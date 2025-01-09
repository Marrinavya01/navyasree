total_salary = sum(employee["salary"] for employee in employees.values())
print(f"Total Salary of Employees: {total_salary}")
# 3. Find the minimum and maximum salaries
salaries = [employee["salary"] for employee in employees.values()]
min_salary = min(salaries)
max_salary = max(salaries)
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")
# 4. Find the employee who is drawing the highest salary
highest_salary_employee = max(employees.values(), key=lambda x: x["salary"])
print(f"Employee with the highest salary: {highest_salary_employee['name']} ({highest_salary_employee['salary']})")
# 5. List employee names whose salary is greater than a dynamic input
threshold = int(input("Enter the salary threshold: "))  # Example: 25000
employees_above_threshold = [
    employee["name"] for employee in employees.values() if employee["salary"] > threshold
]
print(f"Employees earning more than {threshold}: {employees_above_threshold}")