def read_data(filename):
    import csv
    dicdata={}
    with open(filename,'r',newline='') as f:
        dict_csv=csv.DictReader(f)
        list_key=dict_csv.fieldnames
        for row in dict_csv:
            for i in range(len(list_key)):
                if list_key[i] not in dicdata:
                    dicdata[list_key[i]]=[]
                dicdata[list_key[i]].append(row[list_key[i]])
    return dicdata

def test_in_base():
    basecomp={'nom':'Bichon','Prenom':'Bob','adresse':'111 rue de Reuilly'}
    assert basecomp['nom'] in read_data(r'D:\Documents\code\datatest\adresse.csv')['nom']
    assert basecomp['Prenom'] in read_data(r'D:\Documents\code\datatest\adresse.csv')['prenom']