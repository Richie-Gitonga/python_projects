input1 = input("Enter a range of values separated by commas: ")
input2 = input("Enter another set of values separated by commas: ")

def set_generator(values):
    result = set()
    int_values = values.split(",")
    for i in int_values:
        result.add(int(i)) 
    return result

print("Union of A and B: ", set_generator(input1) | set_generator(input2) )

