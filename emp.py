def calculate_gross_salary(basic_salary, hra_rate, da_rate):
    hra = basic_salary * hra_rate / 100
    da = basic_salary * da_rate / 100
    return basic_salary + hra + da


if __name__ == "__main__":
    gross_salary = calculate_gross_salary(50000, 20, 10)
    print("Gross salary:", gross_salary)