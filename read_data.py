
def read_data(filename):
    import csv
    data = {}
    with open(filename, 'r', newline='') as f:
        dict_csv = csv.DictReader(f)
        for row in dict_csv:
            for key in dict_csv.fieldnames:
                if key not in data:
                    data[key] = []
                data[key].append(row[key])
    return data






def ispresent(filename, data):
    d = read_data(filename)
    res = False
    for key in d:
        if data in d[key]:
            res = True
    return res

