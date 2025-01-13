def words_to_numbers(input_str):
    words = input_str.lower().split()
    print(words)
    
    num_dict = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
        "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1000000
    }
    
    result = 0
    current = 0

    for word in words:
        if word in num_dict:
            value = num_dict[word]
            if value == 100:  
                current *= value
            elif value >= 1000:
                current *= value
                result += current
                current = 0
            else:
                current += value
        else:
            raise ValueError(f"Unknown word: {word}")

    result += current
    return result

input_str = "Three hundred million"
print(words_to_numbers(input_str))


print("i am sorry \n" * 100)   #koi string multitime print krni hai 