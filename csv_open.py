import csv
# https://cwsi.pl/python/tutorial/pliki-csv-i-python-odczyt-i-zapis/
def open_csv():
    try:
        with open('Baza.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter = ',')
            names = []
            school = []
            rating = []
            missing_tasks = []

            for row in reader:
                names.append(row['imie'] + " " + row['nazwisko'])
                school.append(row['klasa'])
                rating.append(row['ocena'])
                missing_tasks.append(row['brakujące_zadania'])


    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return names, school, rating, missing_tasks





data = open_csv()
print(type(data))