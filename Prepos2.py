import csv
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# # Download NLTK resources
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove emojis
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U000024C2-\U0001F251]+', '', text)

     # Remove specific words, e.g., "dari" in Bangla
    text = re.sub(r'\bdari\b', '', text, flags=re.IGNORECASE)

   # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]


    return tokens

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header if it exists

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(header + ['Processed Text'])

            for row in reader:
                original_text = row[1]  # Assuming text is in the second column, adjust accordingly
                processed_text = preprocess_text(original_text)
                writer.writerow(row + [' '.join(processed_text)])

# Example usage
input_csv_file = 'dataset/dataset_bng.csv'  # Replace with your CSV file name
output_csv_file = 'dataset/dataset_processed.csv'  # Replace with your desired output file name

process_csv(input_csv_file, output_csv_file)
