import argparse
import urllib.request
import csv
import datetime
import logging

def downloadData(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        return data
    except Exception as e:
        print(f"Error downloading data: {e}")
        exit(1)

def processData(data):
    personData = {}
    csv_reader = csv.reader(data.splitlines())
    next(csv_reader)  # Skip the header row
    for line_num, row in enumerate(csv_reader, start=2):
        try:
            person_id, name, birthday_str = row
            birthday = datetime.datetime.strptime(birthday_str, '%d/%m/%Y').date()
            personData[int(person_id)] = (name, birthday)
        except ValueError:
            logger.error(f"Error processing line #{line_num} for ID #{person_id}")
    return personData

def displayPerson(person_id, personData):
    if person_id in personData:
        name, birthday = personData[person_id]
        formatted_birthday = birthday.strftime('%Y-%m-%d')
        print(f"Person #{person_id} is {name} with a birthday of {formatted_birthday}")
    else:
        print("No user found with that id")

def setupLogger():
    logging.basicConfig(filename='errors.log', level=logging.ERROR, format='Error processing line #%(lineno)d for ID #%(message)s')

def main():
    parser = argparse.ArgumentParser(description='Download and process CSV data.')
    parser.add_argument('--url', required=True, help='URL to the CSV file')
    args = parser.parse_args()

    url = args.url

    setupLogger()

    csvData = downloadData(url)

    personData = processData(csvData)

    while True:
        try:
            user_input = int(input("Enter an ID to lookup (enter a negative number or 0 to exit): "))
            if user_input <= 0:
                break
            displayPerson(user_input, personData)
        except ValueError:
            print("Invalid input. Please enter a valid ID (positive integer) or 0 to exit.")

if __name__ == "__main__":
    main()

