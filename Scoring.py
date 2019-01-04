import csv
import matplotlib.pyplot as plt         #import the necessary libraries
count=0

while True:

    filename='Scores.csv'
    with open(filename) as f:               #open the file and start reading it without reading the headers
        reader=csv.reader(f)
        header_row=next(reader)
        writer=csv.writer(f)

        for row1 in reader:
            if count<4:
                if row1=="":
                    writer.writerow(12)
                    count+=1
filename.close()

