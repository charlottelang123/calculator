from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_multiply():
	assert multiply(2, 3) == 6

def test_subtract():
	assert subtract(3, 2) == 1

def test_CircleArea():
	assert CircleArea(-4) == "Error"

def test_divide_uneven():
	#arrange
	a, b = 5, 2
	#act
	result = divide(a,b)
	#assert
	assert result == 2.5
