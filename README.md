
## Topic
**Classification of harassment in Twitter data.**
This project will classify what type of harassment is happening in a particular text. Ex. Political, gender-related, etc.
Dataset: https://www.kaggle.com/datasets/corinnedavidemakia/emakia-dataset

_twitter-data-tweets.json:_ Raw dataset file (JSON format, processed with Python)

_convert_to_csv.py:_ Converted dataset from JSON to CSV

_cleaned_data.csv:_ Cleaned data with noise removed by data_cleaning.sh

_processed_data.csv:_ Further processed data with tokenization and stopword removal by data_preprocessing.sh

_classification_pipeline.py:_ Python script for classification (TF-IDF, sentiment analysis, Naive Bayes)

_classification_report.txt:_ Output file containing model evaluation results
