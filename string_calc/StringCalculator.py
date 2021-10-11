def add(string):
    delimiter = ','

    if string.startswith('\\'):
        delimiter = string[2]
        string = string[:2]
        print(string)

    #This is to just also split new lines
    string = string.replace('\n', ',')
    print(string)

    string_numbers = string.split(delimiter)
    numbers = []
    for i in string_numbers:
        try:
            number = int(i)
        except ValueError:
            number = 0
        numbers.append(number)

    return sum(numbers)