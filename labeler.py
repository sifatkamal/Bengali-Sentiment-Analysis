import pandas as pd

# Assuming your CSV file is named 'your_file.csv' and has a column named 'text' containing the texts, and a column named 'sentiment' containing 'positive' or 'negative'
df = pd.read_csv('dataset/dataset_processed.csv')

# Define a function to convert sentiments to labels
def sentiment_to_label(sentiment):
    return 1 if sentiment == 'Positive' else 0

# Create a new column 'labels' based on 'sentiment'
df['labels'] = df['Sentiment'].apply(sentiment_to_label)

# Save the updated DataFrame back to a new CSV file or modify the existing one
df.to_csv('dataset_bng_labeled.csv', index=False)