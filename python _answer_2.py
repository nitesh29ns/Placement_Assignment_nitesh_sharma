"""
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
"""

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def valid_string(input:str):
    character_count = {}
    for i in input:
        #print(i)
        if i in character_count.keys():
            character_count[i] +=1
        else :
            character_count[i] = 1
    frecuency = [i for i in character_count.values()]

    for i in frecuency:
        if i > most_frequent(frecuency):
            frecuency[frecuency.index(i)] = i-1
    
    output = None
    for j in frecuency:
        if j == most_frequent(frecuency):
            output = "YES"
        else :
            output = "NO"

    return output


## Test case 1

test_input_1 = "abcdefghhgfedecba"

test_output_1 = valid_string(input=test_input_1)

print(f" test case 1: {test_output_1}")

## Test case 2

test_input_2 = "aabbccddeefghi"

test_output_2 = valid_string(input=test_input_2)

print(f" test case 2: {test_output_2}")