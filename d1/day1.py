from day1and5 import letter_checker

with open ("/main/d1/d1text.txt") as file:


    def number_checker(a_sentence):
        new_string = ""
        for letter in a_sentence:
            if letter in ["1","2","3","4","5","6","7","8","9","0"]:
                new_string += letter

        first_numeric_number = (new_string[0], a_sentence.index(new_string[0]))
        last_numeric_number = (new_string[-1], a_sentence.index(new_string[-1]))

        final_string = new_string[0] + new_string[-1]

        return int(final_string)




    text = file.readlines()
    num_to_sum =[]
    for sentence in text:
        num_to_sum.append(number_checker(sentence))

    my_outcome = sum(num_to_sum)
    print(my_outcome)