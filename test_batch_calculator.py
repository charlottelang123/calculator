from batch_calculator import process_calculation

def test_UNKNOWN_OPERATOR():
    assert process_calculation(".", 2.0, 4.0) == ("ERROR", "", "UNKNOWN_OPERATOR")

def test_INVALID_NUMBER():
    assert process_calculation("*", "A", 6.0) == ("ERROR", "", "INVALID_NUMBER")

def test_DIVISION_BY_ZERO():
    assert process_calculation("/", 4.0, 0.0) == ("ERROR", "", "DIVISION_BY_ZERO")

def test_OK_INPUT():
    assert process_calculation("/", 6.0, 4.0) == ("OK", 1.5, "")
