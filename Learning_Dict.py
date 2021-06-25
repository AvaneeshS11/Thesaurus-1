import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(w):
    w = w.lower()
    # if input word found simply
    if w in data:
        return data[w]
    # if input word is a proper noun (Delhi, Paris, etc)
    elif w.title() in data:
        return data[w.title()]
    # if the input word is an acronym (USA)
    elif w.upper() in data:
        return data[w.upper()]
    # if input word is typo and a close match in found within the data file
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter 'Y if yes and 'N' if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word does not exist please double check. "
        else:
            return "We did not understand your input. "
        
    else:
        return "This word does not exist. Please double check and try again. "
         

# asking user for an input
word = input("Enter a word: ")

output = definition(word)
# creating a more user-friendly output rather than printing full value from dictionary
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
