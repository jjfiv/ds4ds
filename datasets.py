import csv

BOM = '\ufeff'
def clean(string):
    if string.startswith(BOM):
        return string[len(BOM):].strip()
    return string.strip()

def load_titanic():
    titanic = []
    with open('titanic3.csv') as fp:
        table = csv.reader(fp)
        header = [clean(h) for h in next(table)]

        for row in table:
            record = dict((header[i], clean(cell)) for i,cell in enumerate(row))
            titanic.append(record)
    return titanic

