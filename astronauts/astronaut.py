import csv


def get_month():
    astronaut_birth_months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    astronaut_birth_months_counted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open("astronauts.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            birth_date = row[4].split('/')

            for i, one_month in enumerate(astronaut_birth_months):
                if birth_date[0] == one_month:

                    astronaut_birth_months_counted[i] += 1

    get_months_percentages(astronaut_birth_months_counted, astronaut_birth_months)

    return


def get_months_percentages(astronaut_month_count, months_final):

    astronaut_months_percentage = []

    for one_month in astronaut_month_count:
        astronaut_months_percentage.append(one_month / sum(astronaut_month_count) * 100)

    find_3_most_popular(astronaut_months_percentage, months_final)

    return


def find_3_most_popular(months_percentage, month_final):
    top_months = list(sorted(zip(months_percentage, month_final), reverse=True)[:3])

    for i, one_month in enumerate(top_months):
        print(f'A(z) {i + 1}. leggyakoribb születési hónap: {one_month[1]}., '
              f'ez {round(one_month[0], 1)}%-os arányban jelenik meg.')


def main():
    print('A program egy .csv file-ból kiolvassa űrhajósok születési dátumait és meghatározza, '
          'hogy melyik a három leggyakoribb születési hónap.\n')
    get_month()


main()
