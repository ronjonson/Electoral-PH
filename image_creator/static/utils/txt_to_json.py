import json

provinces = {}

with open(r"results\data\provinces-svg.txt", encoding='utf-8') as f:
    for line in f:
        data = line.split(":")
        if data[0] != 'province':
            try:
                provinces[data[0]] = data[1]
            except:
                print("ERROR")
                print(line)
        

with open("provinces.json", "w") as f:
    json.dump(provinces,f)
