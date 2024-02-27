user_input = input("Enter a sequence of numbers separated by a comma: ")

user_list = user_input.split(",")

list_input = [int(x) for x in user_list]

print(list_input)

