"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""
"""Return (status, result, error_code) for one calculation.

Inputs are strings. Trim whitespace and use the four imported lab functions.
Success: ("OK", numeric_result, "").
The error_code is empty on success because there is no error to report.
Error: ("ERROR", "", error_code).

Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
See the brief for the full contract. You may add small helper functions.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):

    error_code = ""
    status = "OK"
    result = ""

    if type(a_text) != float or type(b_text) != float:
        status = "ERROR"
        error_code = "INVALID_NUMBER"

    elif operation == "/":

        if b_text == 0:
            status = "ERROR"
            error_code = "DIVISION_BY_ZERO"
        else:
            result = divide(a_text,b_text)

    elif operation == "+":
        result = add(a_text, b_text)
    
    elif operation == "-":
        result = subtract(a_text,b_text)

    elif operation == "*":
        result = multiply(a_text,b_text)

    else:
        status = "ERROR"
        error_code = "UNKNOWN_OPERATOR"
    
    return status, result, error_code
    



