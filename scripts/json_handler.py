import csv
import json

def load_json(fp):
    with open(fp) as f:
        json_data = json.load(f)
    return json_data

def json_out(data, output_fp):
    with open(output_fp, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)

def data_to_json(input_fp):
    jsonArray = []
    with open(input_fp, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            jsonArray.append(row)
    json_out(jsonArray, 'data/TrainingDS.json')

