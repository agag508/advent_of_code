def floor_counter(an_instruction):
    current_floor = 0
    current_index = 0



    for element in an_instruction:
        if current_floor == -1:
            return current_index
        elif element == "(":
            current_floor += 1
            current_index += 1
        elif element == ")":
            current_floor -= 1
            current_index += 1
        else:
            current_index += 1



    return "End"


with open("floors.txt", "r") as file:
    my_text = file.read()
    print(floor_counter(my_text))
"""
print(floor_counter("()())"))"""