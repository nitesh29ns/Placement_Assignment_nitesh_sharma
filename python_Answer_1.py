""""
Question 1: -
Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.

"""
def  len_of_highest_frequency_word(input:str):
    count_dict = {}
    for i in input.split(" "):
        if i in count_dict.keys():
            count_dict[i] +=1
        else:
            count_dict[i] = 1

    word_count = [i for i in count_dict.values()]
    word_count.sort()
    highest_frequency_word = word_count[-1]
    len_of_word = []
    for word in count_dict.keys():
        if highest_frequency_word == count_dict[word]:
            #print(word)        # for display highest_frequency_word.
            len_of_word.append(len(word))

    len_of_word.sort()

    return len_of_word[-1]

## Test case 1

test_input_1 = "She lived in a big house with a big garage on the outskirts of a big city"

test_output_1 = len_of_highest_frequency_word(input=test_input_1)
print(f"test case 1: {test_output_1}")

## Test case 2

test_input_2 ="There are many animals at the zoo My daughter has many toys My son has many baseball cards My teacher has many pencils"

test_output_2 = len_of_highest_frequency_word(input=test_input_2)
print(f" test case 2 : {test_output_2}")
