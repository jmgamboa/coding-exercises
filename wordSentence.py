
def howMany(sentence):
    word_count = 0
    punctuation_list = [',', '.', '!', '?']

    curr_string = ""
    for idx, i in enumerate(sentence):
        curr_char = i
        curr_string += i
        if curr_char == ' ' and sentence[idx+1] != ' ' or (idx == len(sentence)-1):
            curr_string = curr_string.replace(" ", "")
            if curr_string.isalpha():
                word_count += 1
            elif '-' in curr_string:
                word_count += 1
            elif any(el in curr_string for el in punctuation_list):
                word_count += 1
            curr_string = ""
    return word_count



x = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"



s1 = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"

print(howMany(s1))