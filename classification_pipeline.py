import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from textblob import TextBlob
import chardet
import scipy.sparse

# File Paths
PROCESSED_FILE = "Dataset/twitter_data/processed_data.csv"

# Step 1: Detect and Handle Encoding Issues
print("Detecting file encoding...")
with open(PROCESSED_FILE, "rb") as file:
    result = chardet.detect(file.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# Step 2: Load Processed Data with Detected Encoding
print("Loading processed data...")
data = pd.read_csv(
    PROCESSED_FILE,
    names=["id", "text", "category"],
    encoding=encoding,
    on_bad_lines='skip',
    sep=','
)

# Step 3: Filter Infrequent Categories
print("Filtering infrequent categories...")
min_samples = 5  # Minimum number of samples per category
data = data[data['category'].map(data['category'].value_counts()) >= min_samples]

# Step 4: Add Sentiment Features
print("Adding sentiment features...")
def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity, blob.sentiment.subjectivity

data[['polarity', 'subjectivity']] = data['text'].apply(lambda x: pd.Series(get_sentiment(x)))

# Normalize sentiment features to be non-negative
print("Normalizing sentiment features...")
data['polarity'] = data['polarity'] - data['polarity'].min()  # Shift to make all values non-negative
sentiment_features = scipy.sparse.csr_matrix(data[['polarity', 'subjectivity']].values)

# Step 5: TF-IDF Vectorization
print("Applying TF-IDF vectorization...")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_text = vectorizer.fit_transform(data["text"].astype(str))

# Combine TF-IDF and sentiment features
X = scipy.sparse.hstack([X_text, sentiment_features])

# Step 6: Encode Target Labels
print("Encoding category labels...")
y = data["category"].astype(str)

# Step 7: Train-Test Split
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Train Naive Bayes Classifier
print("Training Naive Bayes classifier...")
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 9: Evaluate Model
print("Evaluating model...")
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=1))

# Save classification report to file
with open("classification_report.txt", "w") as f:
    f.write(classification_report(y_test, y_pred, zero_division=1))
