from StringCalculator import add

def test_return_0_for_empty_string():
	result = add("") 
	assert result == 0

def test_single_numbers():
	result = add("1")
	assert result == 1

	result = add("22")
	assert result == 22

def test_string_multple_numbers_return_sum():
	result = add("1, 2")
	assert result == 3

	result = add("3, 2, 5")
	assert result == 10

	result = add("1,2,3,4,5")
	assert result == 15

def test_newline_delimiter():
	result = add("1\n2,3")
	assert result == 6

def test_different_delimiters():
	result = add("//;\n1,2")
	assert result == 3

def test_negative_numbers_raises_exception():
	result = add("-1")
	assert ValueError