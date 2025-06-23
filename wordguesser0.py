print("Start")
import json
dictionaryfile = "./assets/words_dictionary.json"
with open(dictionaryfile) as dictfile:
    print("Loading Data")
    dictionarydata = json.load(dictfile)
    print("Data loaded")

def main():
    print(dictionarydata)
    

main()

print("End")