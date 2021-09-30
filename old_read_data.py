def read_data(filename):
    import csv
    dicdata = {}
    with open(filename, 'r', newline='') as f:
        dict_csv = csv.DictReader(f)
        list_key = dict_csv.fieldnames
        for row in dict_csv:
            for i in range(len(list_key)):
                if list_key[i] not in dicdata:
                    dicdata[list_key[i]] = []
                dicdata[list_key[i]].append(row[list_key[i]])
    return dicdata


# Test

test_data = input('Entrer un nom, un prenom ou une adresse ?')

if test_data in read_data(r'D:\Documents\code\datatest\adresse.csv')['nom']:
    print(True)
elif  test_data in read_data(r'D:\Documents\code\datatest\adresse.csv')['prenom']:
    print(True)
elif test_data in read_data(r'D:\Documents\code\datatest\adresse.csv')['adresse']:
    print(True)

else:
    print(False)