import csv
row=[]
peop_1=()

peo_2=()
total_peop_2=int()

peo_3=()
total_peop_3=int()

total_peop_4=int()

total_peop_5=int()

with open("data.txt", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        if row[4].startswith("Oman"):
            peop_1 = int(row[6])
print("1 uzdevus: ", peop_1)

with open("data.txt", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        if row[4].startswith("Latvia"):
            peop_2=int(row[8])
            total_peop_2 += peop_2
print("2 uzdevus: ", total_peop_2)

with open("data.txt", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        if row[4].startswith("Latvia"):
            if row[7].startswith("Telecommunications"):
                peop_3=int(row[8])
                total_peop_3 += peop_3
print("3 uzdevus: ", total_peop_3)

with open("data.txt", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        if row[4].startswith("Latvia"):
            if row[3].startswith("http://"):
                
                total_peop_4 += 1
print("4 uzdevus: ", total_peop_4)

with open("data.txt", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        if row[4].startswith("Latvia"):
            if row[3].endswith(".org/"):
                
                total_peop_5 += 1
print("5 uzdevus: ", total_peop_5)