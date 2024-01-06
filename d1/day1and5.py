
text = ['two1nine','eightwothree','abcone2threexyz',
            'xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']


def letter_checker(a_sentence):
    str_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                   'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = str_numbers.keys()
    numbers_and_indexes = []

    for number in numbers_list:
        if number in a_sentence:

            numbers_and_indexes.append((str_numbers[number], a_sentence.index(number[0])))  # a numeric value, an index
                                                                                         ##  of a world
    return numbers_and_indexes

    for n in range(len(text)):

        print(letter_checker(text[n]))



