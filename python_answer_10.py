#necessary imports

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


def part_of_speech_taging(input:str):
    tags = pos_tag(word_tokenize(input),lang="eng") 

    dic = {"nouns":0,
       "prononus":0,
       "verbs":0,
       "adjectives":0}
    
    for i in tags:
        if i[-1] == "NN" or i[-1] =="NNS" or i[-1] =="NNP" or i[-1] =="NNPS":
            dic['nouns'] = dic['nouns']+1
        elif i[-1] == "PRP" or i[-1] =="PRP$":
            dic['prononus'] = dic['prononus']+1
        elif i[-1] == "VBZ" or i[-1] =="VB" or i[-1] =="VBG" or i[-1] =="VBD" or i[-1] =="VBN" or i[-1] =="VBP":
            dic['verbs'] = dic['verbs']+1
        elif  i[-1] == "JJ" or i[-1] == "JJR" or i[-1] =="JJS":
            dic['adjectives'] =dic['adjectives']+1

    return dic



## Test case 1

test_input_1 = "The adventurous traveler embarked on a thrilling expedition to the remote mountains. With a determined stride, he scaled steep cliffs, crossed roaring rivers, and explored hidden caves. The magnificent scenery left him in awe, as he gazed at majestic peaks, lush green valleys, and cascading waterfalls. The intrepid explorer captured breathtaking photographs of the breathtaking landscapes, capturing their beauty for posterity."

test_output_1 = part_of_speech_taging(input=test_input_1)

print(f" test case 1: {test_output_1}")

## Test case 2

test_input_2 = "He eagerly shared his remarkable journey with friends and family, recounting tales of daring escapades and incredible encounters. They listened intently, captivated by his vivid descriptions and animated gestures. His courage and perseverance inspired them, igniting a desire for their own exciting quests."

test_output_2 = part_of_speech_taging(input=test_input_2)

print(f" test case 2: {test_output_2}")