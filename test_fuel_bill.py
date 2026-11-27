from fuel_bill import calculate_fuel_cost


def test_petrol_cost():
    assert calculate_fuel_cost(10, 105.0) == 1050.0


def test_diesel_cost():
    assert calculate_fuel_cost(20, 90.0) == 1800.0


def test_fractional_litres():
    assert calculate_fuel_cost(2.5, 100.0) == 250.0