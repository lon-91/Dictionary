import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes,or n if no " % get_close_matches(word, data.keys())[0])
    if yn == "y":
        return data[get_close_matches(word, data.keys())[0]]
    elif yn == "n":
        return "Word doesn't exist.Please double check it."
    else:
        return "we didn't understand your entry."
   # else:
     # return "Word doesn't exist.Please double check it"


word = input("Enter a word:  ").lower().capitalize()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

    else:
        print(output)
