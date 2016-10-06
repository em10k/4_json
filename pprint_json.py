import json
import pprint

def pretty_print():
    with open('bars.json','r', encoding='utf-8') as task:
        line=task.read()
        line=line.split (',') 
        line.insert(0, line[:])
        pp = pprint.PrettyPrinter(indent=4)
        print(json.dumps(line, sort_keys=True, indent=4))

if __name__ == '__main__':
	pretty_print()
