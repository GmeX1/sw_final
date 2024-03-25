import sqlite3
import csv

INDEXES = {
    'id': 'no',
    'no': 'no',
    'galaxy': 'galaxy',
    'sign': 'galaxy',
    'type': 'type',
    'type_id': 'type',
    'luminosity': 'luminosity',
    'luminosity_id': 'luminosity',
    'range': 'luminosity',
    'size': 'size',
    'stars': 'stars'
}

db = sqlite3.connect(input())
table, field = input().split('.')
min_val = min(map(lambda x: x[0], db.cursor().execute(f'SELECT {field} from {table}').fetchall()))

out_dicts = list()
for string in db.cursor().execute('SELECT * FROM galaxies').fetchall():
    str_dict = dict()
    str_dict['no'] = string[0]
    str_dict['galaxy'] = string[1]
    str_dict['type'] = string[2]
    str_dict['size'] = string[3]
    str_dict['luminosity'] = string[4]
    str_dict['stars'] = string[5]
    if str_dict[INDEXES[field]] == min_val:
        str_dict['type'] = db.cursor().execute(f'SELECT type FROM types where id={string[2]}').fetchone()[0]
        str_dict['luminosity'] = db.cursor().execute(f'SELECT range FROM luminosities where id={string[4]}'
                                                     ).fetchone()[0]
        out_dicts.append(str_dict)

with open('collisions.csv', 'w') as f:
    writer = csv.DictWriter(f, ['no', 'galaxy', 'type', 'luminosity', 'size', 'stars'], delimiter='#')
    writer.writeheader()
    writer.writerows(out_dicts)
