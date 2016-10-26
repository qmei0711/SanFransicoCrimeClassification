import csv


def dateConversion(date):
    parts = date.split()
    sections = parts[1].split(':')
    if 0 <= int(sections[0]) <= 6:
        return 'Late Night'
    elif 7 <= int(sections[0]) <= 12:
        return 'Morning'
    elif 13 <= int(sections[0]) <= 18: 
        return 'Afternoon'
    else:
        return 'Evening'

def process(readFile, writeFile):
    map = {}
    with open(readFile, 'rb') as rFile, open(writeFile, 'wb') as wFile:
        fieldnames = ['Category','Time','DayOfWeek', 'PdDistrict']
        reader = csv.DictReader(rFile)
        writer = csv.DictWriter(wFile, fieldnames=fieldnames)
        writer.writeheader()
        c1, c2 = 0, 0
        for row in reader:
            if row['Category'] == 'LARCENY/THEFT':
                c1 += 1
                writer.writerow({'Category':1, 'Time':dateConversion(row['Dates']), 'DayOfWeek':row['DayOfWeek'], 'PdDistrict':row['PdDistrict']})
            elif row['Category'] != 'LARCENY/THEFT' and c2 < 200000:
                c2 += 1
                writer.writerow({'Category':0, 'Time':dateConversion(row['Dates']), 'DayOfWeek':row['DayOfWeek'], 'PdDistrict':row['PdDistrict']})
        # print res


def main():
    process("../../data/train.csv", "../../data/refinedTrain.csv");

if __name__ == '__main__':
    main()