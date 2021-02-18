import json

with open('ato.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

value = text.values()

def rozvorot(list):
    return list[::-1]


def recursive(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            recursive(value)
    elif isinstance(obj, list):
        for item in obj:
            if type(item[0]) == float:
                rozvorot(item)
            recursive(item)
    else:
        print(obj)

if __name__ == '__main__':
    print(recursive(text))

    if type(item[0]) == float:
        print(rozvorot(item))
