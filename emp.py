import sys

def calculate_gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    return basic_salary + hra + da

if __name__ == "__main__":
    basic_salary = float(sys.argv[1])
    gross_salary = calculate_gross_salary(basic_salary)
    print("Basic Salary:", basic_salary)
    print("Gross Salary:", gross_salary)