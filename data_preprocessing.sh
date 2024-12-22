
#!/bin/bash
# Data Preprocessing Script for Cleaned Data

# Input and Output Files
CLEANED_FILE="Dataset/twitter_data/cleaned_data.csv"
PROCESSED_FILE="Dataset/twitter_data/processed_data.csv"

# Step 1: Tokenize Text (Split sentences into words)
echo "Tokenizing text..."
awk -F',' '{
    split($2, words, " ");
    for (i in words) {
        print $1 "," words[i] "," $3;
    }
}' "$CLEANED_FILE" > temp_tokenized.csv

# Step 2: Remove Stop Words (Requires stopwords.txt)
echo "Removing stop words..."
if [ ! -f stopwords.txt ]; then
    echo "Error: stopwords.txt file is missing! Please provide a file with stop words."
    exit 1
fi
grep -vwFf stopwords.txt temp_tokenized.csv > "$PROCESSED_FILE"

# Cleanup Intermediate Files
echo "Cleaning up temporary files..."
rm temp_tokenized.csv

echo "Data preprocessing completed! Preprocessed data saved to: $PROCESSED_FILE"
