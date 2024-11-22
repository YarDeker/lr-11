import csv
import os

try:
    with open("Lab11.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data = list(reader)
        
        print("Country Name; 2018; 2019")
        for row in data:
            print(f"{row['Country Name']}; {row['2018']}; {row['2019']}")

        countries = input("Введіть назви країн через кому: ").split(',')
        countries = [country.strip().lower() for country in countries]

        search_results = [row for row in data if row['Country Name'].strip().lower() in countries]
 
        if search_results:
            print("\nЗнайдені результати:")
            for result in search_results:
                print(f"{result['Country Name']}: 2018: {result['2018']}, 2019: {result['2019']}")
                output_file = 'results.csv'
                with open(output_file, "a", newline='') as output_csvfile:
                    writer = csv.writer(output_csvfile, delimiter=";")
                    writer.writerow((result["Country Name"], result["2018"], result["2019"]))  
            print(f"\nРезультати записано у файл: {output_file}")
        else:
            print("\nКраїни не знайдено в базі даних.")
except Exception as e:
    print(f"Сталася непередбачена помилка: {e}")
