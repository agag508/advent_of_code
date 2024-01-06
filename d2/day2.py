
def calculate_params():

    with open("papa.txt", "r") as file:
        text = file.readlines()
        working_list =[]
        result_list =[]
        #line_counter = 0

        for line in text:
            current_letter =""
            #line_counter += 1

            for letter in line:


                if letter in ["1","2","3","4","5","6","7","8","9", "0"]:
                    current_letter += letter
                elif letter =="\n":
                    working_list.append(int(current_letter))
                    result_list += [working_list]
                    working_list = []
                else:
                    working_list.append(int(current_letter))
                    current_letter = ""
                    continue


    return result_list


calculated_params = calculate_params()


def paper(l, w, h):
    smallest = [l,w,h]
    smallest.sort()

    total_paper = 2*l*w + 2*w*h + 2*h*l + smallest[0] * smallest[1]
    return total_paper



result= 0

for param in calculated_params:
    result += paper(param[0], param[1], param[2])
print(result)
print(calculated_params[-1])
