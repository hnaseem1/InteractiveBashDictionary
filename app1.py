#essential libraries
import json
from difflib import get_close_matches

#loads JSON data
data = json.load(open("data.json"))

#Function to find word in the data with cetain rules
def translate(w):

    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
 
# match the user input with the data for similar words (get_close_matches returns a list using similarity ratios in descending order)
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            
#returns the first word from the suggestions (the first one is the most similar one)
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, please double check.."
        else:
            return "We didn't understand your entry.."
    else:
        return "The word doesn't exist, please double check.."

#Initialize 
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
