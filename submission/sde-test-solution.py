import json, os, sys

# input_path = os.environ['input_path']
# output_path = os.environ['output_path']

input_path = sys.argv[1]
output_path = sys.argv[2]

if len(sys.argv) > 3:
    raise Exception("Can only accept input and output file names as input!")

with open(input_path) as j:
    data = json.load(j)

data = data['data']

if len(data) <= 0:
    raise Exception("Input data is not valid. Please check")

# filter all the corporate bonds which are having null yield
dic_bonds = {}
for _data in data:
    if _data['yield'] != None and _data['id'][0:1] == 'c':
        dic_bonds[_data['id']] = []

# get all the posible combinations of corporate and goverment bonds to be compared
for key in dic_bonds.keys():
    for _data in data:
        if _data['yield'] != None and _data['id'][0:1] == 'g':
            dic_bonds[key].append(_data['id'])

tenor_data = {}
yield_data = {}
# store tenor data in dic
for _data in data:
    tenor_data[_data['id']] = _data['tenor'].replace(' years', '')
    if _data['yield'] != None :
        yield_data[_data['id']] = _data['yield'].replace('%', '')

# comparison results
comp_dic = {}
results = {}
output = []

for key, value in dic_bonds.items():
    for _value in value:
        results[key+'-'+_value] = abs(float(tenor_data[key]) - float(tenor_data[_value]))
    # get minimum of tenor between corporate and government bonds
    mins = min(results.items(), key=lambda x: x[1])[0].split('-')
    results = {}
    output.append({"corporate_bond_id": mins[0], "government_bond_id": mins[1], "spread_to_benchmark": round(abs(float(yield_data[mins[0]]) - float(yield_data[mins[1]])) * 100)})

print({"data": output})

with open(output_path, 'w') as outfile:
    json.dump({"data": output}, outfile)

