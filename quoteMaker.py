import csv
f=open("Quotes.csv")
out=open("quotes.txt","w")

csv_reader=csv.reader(f,delimiter=';')
out.write('[')

#skip first line
for row in csv_reader:
    break
for row in csv_reader:
    out.write("\""+row[0]+" -"+row[1]+"\",")

out.write(']')

f.close()
out.close()