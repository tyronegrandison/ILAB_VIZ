#!/usr/bin/env python
import csv
import json

keepers = ["Goods", "Description", "Country", "Region", "Children Working and Studying (7-14 yrs old)", "Year", "Advancement_Level", "Education Statistics: Attendance Statistics", "Children's Work Statistics"]

def load_json(file):
    with open(file) as data_file:
        data = json.load(data_file)
        return data

def print_types():
    data = load_json("../data/countries2013.json")
    s_data = []
    for k in data:
        clipped_country = {}
        for i in k:
            for keep in keepers:
                if i == keep:
                    clipped_country[keep] = k[keep]
        s_data.append(clipped_country)

    dump_to_json(s_data)

def dump_to_json(data_dict):
    with open('../clipped.json', 'w') as outfile:
        json.dump(data_dict, outfile)

print_types()
