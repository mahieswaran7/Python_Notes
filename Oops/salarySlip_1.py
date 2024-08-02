class Salary:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

class Allowances(Salary):
    def calculate_allowances(self):
        HRA = 0.20 * self.basic_salary
        DA = 0.40 * self.basic_salary
        TA = 0.25 * self.basic_salary
        return HRA + DA + TA

class Deductions(Salary):
    def calculate_deductions(self):
        insurance = 5000
        pf = 0.12 * self.basic_salary
        gratuity = 0.05 * self.basic_salary
        return insurance + pf + gratuity

class CalculateSalary:
    def __init__(self, basic_salary):
        self.salary = Salary(basic_salary)
        self.allowances = Allowances(basic_salary)
        self.deductions = Deductions(basic_salary)
    
    def calculate_gross_salary(self):
        return self.salary.basic_salary + self.allowances.calculate_allowances()

    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        deductions = self.deductions.calculate_deductions()
        return gross_salary - deductions

    def print_salary_slip(self):
        gross_salary = self.calculate_gross_salary()
        deductions = self.deductions.calculate_deductions()
        net_salary = self.calculate_net_salary()
        print(f"Basic Salary: \u20B9{self.salary.basic_salary:.2f}")
        print( )
        print(f"Allowances: \u20B9{self.allowances.calculate_allowances():.2f}")
        print( )
        print(f"Gratuity: \u20B9{0.05 * self.salary.basic_salary:.2f}")
        print( )
        print(f"Deductions: \u20B9{deductions:.2f}")
        print( )
        print(f"Gross Salary: \u20B9{gross_salary:.2f}")
        print( )
        print(f"Net Salary: \u20B9{net_salary:.2f}")

if __name__ == "__main__":
    basic_salary = float(input("Enter basic salary: \u20B9"))
    calculator = CalculateSalary(basic_salary)
    calculator.print_salary_slip()

