import csv
import re


#export csv->tsv
with open('population.csv','r') as csvin, open('population.txt', 'w') as tsvout:
   csvin = csv.reader(csvin)
   tsvout = csv.writer(tsvout, delimiter='\t')
   for row in csvin:
       tsvout.writerow(row)
f=open('population.txt', "r")
a=f.read()
print(a)


#csv without headers
with open('population.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['mac-address'],'\t', row['hostname'],'\t', row['ipv4'],'\t', row['ipv6'],\
              '\t', row['netmask'],'\t', row['user'],'\t', row['full name'],'\t', row['email'],\
              '\t', row['ssh private key'],'\t', row['description host'],'\t', row['list of apps'])


#filter by list
with open('population.csv') as csvin:
    csv_reader = csv.reader(csvin)
    rows = list(csv_reader)
    print('\r',rows[2],'\n',rows[4])

#filter by a string,  1 field. regex
with open('population.csv', newline='') as f:
     reader = csv.reader(f)
     for row in reader:
         a=re.match("\w+\.+\w+@([a-zA-Z])+.([a-zA-Z]){3}", row[5])
         if a:
             print(a.string)
     data=" ".join(row[5] for row in reader)
    print(data)


#filter by a string, multi field. regex
with open('population.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        a = ' '.join(row)
        for m in re.finditer("\w+\.+\w+@([a-zA-Z])+.([a-zA-Z]){3}", f.readline()):
            print(m.group(0))


#data field
single_string=[]
with open('population.csv', newline='') as f:
     reader = csv.reader(f)
     for row in reader:
         for item in row:
             single_string.append(item)
     print(single_string)
