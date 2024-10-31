import sys
import csv

def read_data(soubor):
      data = []
      with open(soubor, "r") as file:       #otevre soubor, r mode a priradi to file
        reader = csv.reader(file)           #reader - csv.funkce z knihovny csv
        for radek in reader:                #
            data.append(radek)
        return data

def read_data_split(soubor):
      data = []
      with open(soubor, "r") as file:        #otevre soubor, r mode a priradi to file
        for line in file:
            data.append(line.strip())
        return data

def write_data(soubor, data):
    with open(soubor, "w", newline="") as file:     #otevre soubor, write mode a priradi to jako file
        for row in data:
            line = ''.join(row) + '\n'
            file.write(line)



if __name__ == "__main__":
    try:
        file = sys.argv[1]
        data = read_data(file)
        print(data)
        data = read_data_split(file)
        print(data)
        write_data("excel3.csv", data)
    except IndexError:
        print("Nebyly zadány soubory.")
    except FileNotFoundError:
        print("Zadany soubor neexistuje.")
