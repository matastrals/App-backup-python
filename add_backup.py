import json

def main():
    writeToJson()

def writeToJson():
    with open('state.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data['2z4Qda13a'] = {}
    data['2z4Qda13a']['time'] = '15:22'
    data['2z4Qda13a']['path'] = '/home/test'
    with open('state.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()