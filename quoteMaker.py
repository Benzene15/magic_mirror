import csv
f=open("Quotes.csv")

csv_reader=csv.reader(f,delimiter=';')
quote=""

#skip first line
for row in csv_reader:
    break
i=0
for row in csv_reader:
    quote=(row[0]+" -"+row[1])
    i+=1
print(i)

f.close()