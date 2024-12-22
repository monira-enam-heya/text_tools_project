
#!/bin/bash
# Data Cleaning Script for Preconverted CSV Data

# Input and Output Files
INPUT_FILE="Dataset/twitter_data/twitter-data.csv"  
CLEANED_FILE="Dataset/twitter_data/cleaned_data.csv"

# Step 1: Remove URLs, Mentions, and Special Characters
echo "Cleaning text fields..."
sed -E 's/http[^ ]+//g' "$INPUT_FILE" | sed -E 's/@[a-zA-Z0-9_]+//g' | sed -E 's/[^a-zA-Z0-9, ]//g' > "$CLEANED_FILE"

echo "Data cleaning completed! Cleaned data saved to: $CLEANED_FILE"
