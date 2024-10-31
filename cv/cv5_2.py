import sys

def read_data(file_name):
    data = []
    # TODO
    return data

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        data = read_data(file)
        print(data)
    except IndexError:
        print("Nebyly zadány soubory.")
    except FileNotFoundError:
        print("Zadany soubor neexistuje.")
