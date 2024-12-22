
## Topic
**Classification of harassment in Twitter data.**
This project will classify what type of harassment is happening in a particular text. Ex. Political, gender-related, etc.
Dataset: https://www.kaggle.com/datasets/corinnedavidemakia/emakia-dataset
twitter-data-tweets.json: Raw dataset file (JSON format, processed with Python)
convert_to_csv.py: Converted dataset from JSON to CSV
cleaned_data.csv: Cleaned data with noise removed by data_cleaning.sh
processed_data.csv: Further processed data with tokenization and stopword removal by data_preprocessing.sh
classification_pipeline.py: Python script for classification (TF-IDF, sentiment analysis, Naive Bayes)
classification_report.txt: Output file containing model evaluation results