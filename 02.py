import argparse
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument('--type', default='elliptical', type=str)
parser.add_argument('--file', type=str, required=True)

args = parser.parse_args()
with open(args.file) as f:
    data = csv.DictReader(f, delimiter=':')
    data_filtered = list(filter(lambda x: x['type'] == args.type, data))
json_dict = dict()
for item in data_filtered:
    json_dict[item['galaxy']] = round(int(item['dark']) / int(item['mass']), ndigits=1)

with open('relations.json', 'w') as f:
    json.dump(json_dict, f)
