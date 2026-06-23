# Employee Payroll System
emp_ids = [111,222,333]
emp_details = {
    111 : {"Name":"Jiya","Role":"AI Engineer"},
    222 : {"Name":"Ishika","Role": "Software Developer"},
    333: {"Name":"Bhoomika", "Role":"Software Designer"}
}
def calculate_allowance(basic_salary):
    return basic_salary * 0.20

def calculate_deduction(basic_salary):
    return basic_salary * 0.10

class EmployeeSalary:
    def __init__(self, emp_id, basic_salary):
        self.emp_id = emp_id
        self.basic = basic_salary
        self.allowance = calculate_allowance(self.basic)
        self.deduction = calculate_deduction(self.basic)
        self.net_salary = self.basic + self.allowance - self.deduction
    def display_report(self):
        details = emp_details[self.emp_id]
        print(f"ID: {self.emp_id} | Name: {details['Name']} | Role: {details['Role']}")
        print(f"  Basic: {self.basic:.2f}")
        print(f"  Allowance (+20%): {self.allowance:.2f}")
        print(f"  Deduction (-10%): {self.deduction:.2f}")
        print(f"  Net Salary Paid: {self.net_salary:.2f}")

processed_employees = []

print(" Enter Salary Details ")
for emp_id in emp_ids:
    name = emp_details[emp_id]["Name"]
    while True:
        try:
            salary_input = input(f"Enter basic salary for {name} (ID {emp_id}): ")
            basic_salary = float(salary_input)
            
            if basic_salary <= 0:
                raise ValueError("Salary must be a positive number greater than zero.")
            
            emp_payroll = EmployeeSalary(emp_id, basic_salary)
            processed_employees.append(emp_payroll)
            break
            
        except ValueError as error:
            print(f"Invalid Input. Please try again.\n")


print("\n FINAL PAYROLL REPORT ")
for emp in processed_employees:
    emp.display_report()