import pandas as pd
import json

# Input JSON file
input_file = "Dataset/twitter_data/twitter-data-tweets.json"
output_file = "Dataset/twitter_data/twitter-data.csv"

try:
    # Load JSON file with explicit encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Convert to DataFrame
    df = pd.json_normalize(data)

    # Filter for relevant columns
    df = df[['id', 'text', 'lang', 'category']]

    # Save only English tweets to CSV
    df[df['lang'] == 'en'].to_csv(output_file, index=False)

    print(f"CSV file saved to {output_file}")
except UnicodeDecodeError as e:
    print(f"Encoding issue: {e}")
    print("Ensure the JSON file is encoded in UTF-8.")
