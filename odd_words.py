words_input = input("Enter a sequence of words separated by a comma: ")

words = words_input.split(",")
print(type(words))

def odd_validator(values):
    result = []
    for value in values:
        if(len(value) % 2 != 0):
            result.append(value)
        else:
            continue
    return result

result = odd_validator(words)
print(result)


