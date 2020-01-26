import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        k = get_close_matches(word, data.keys())[0] 
        print("are you looking for : " + k) 
        print("Enter yes if ..")
        k1 = input()
        if k1=='yes':
            return data[k]
        else:
            return "Sorry check it again."    
    else: 
        return "The Word doesn't exit..."    

word = input("Enter word : ")

output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print("Word Does not exits!")        
