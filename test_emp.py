from emp import calculate_gross_salary


def test_calculate_gross_salary():
    assert calculate_gross_salary(50000, 20, 10) == 65000
