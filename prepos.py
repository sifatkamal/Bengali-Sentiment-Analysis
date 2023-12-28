import csv
import random

def process_text_files(pos_file, neg_file, output_csv):
    # Open the positive text file for reading
    with open(pos_file, 'r', encoding='utf-8') as pos_file:
        pos_lines = pos_file.readlines()

    # Open the negative text file for reading
    with open(neg_file, 'r', encoding='utf-8') as neg_file:
        neg_lines = neg_file.readlines()

    # Combine positive and negative lines
    combined_lines = [(line.strip(), 'Positive') for line in pos_lines] + [(line.strip(), 'Negative') for line in neg_lines]

    # Shuffle the combined lines randomly
    random.shuffle(combined_lines)

    # Open the CSV file for writing
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header if needed
        # csv_writer.writerow(['Label', 'Text'])  # Uncomment this line if you want a header

        # Write each line with its corresponding label
        for line, label in combined_lines:
            # Write the labeled example to the CSV file
            csv_writer.writerow([label, line])

if __name__ == "__main__":
    # Specify the paths to your positive and negative text files
    positive_text_file = 'dataset/all_positive_8500.txt'
    negative_text_file = 'dataset/all_negative_3307.txt'

    # Specify the path to the output CSV file
    output_csv_file = 'dataset/dataset_bng.csv'

    # Process the text files and create the CSV file
    process_text_files(positive_text_file, negative_text_file, output_csv_file)
