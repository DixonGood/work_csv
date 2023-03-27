import json
import csv
import random

dict = {
    312456: ("Astin", 17),
    134567: ("Bob", 21),
    324512: ("Martin", 27),
    534123: ("Meddison",12),
    456789: ("David", 40),
    567890: ("Emma", 45),
}

with open('homework1.json', "w") as file:
    json.dump(dict, file)

with open('homework1.json', "r") as file:
    data = json.load(file)

with open('homework2.csv', 'w', newline='') as csvfile:
    writer_file = csv.writer(csvfile)

    writer_file.writerow(['ID', "Имя", "Возраст", "Телефон"])

    for key, value in data.items():
        name, age = value
        phone = ''.join([str(random.randint(0,9)) for _ in range(10)])
        writer_file.writerow([key, name, age, phone])