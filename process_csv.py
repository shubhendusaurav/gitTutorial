import csv
import os

def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def process_data(data):
    """
    Processes data: Adds a new column 'Processed' and sets it to 'Yes'.
    """
    for row in data:
        row['Processed'] = 'Yes'
    return data

def write_csv(data, output_file_path):
    """
    Writes processed data to a new CSV file.
    """
    if not data:
        raise ValueError("No data to write.")

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    try:
        print("Reading input file...")
        data = read_csv(input_file)
        
        print("Processing data...")
        processed_data = process_data(data)
        
        print("Writing output file...")
        write_csv(processed_data, output_file)
        print(f"Processed data has been written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
