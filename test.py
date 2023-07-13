import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing functions
def preprocess_text(text):
    # Tokenize text into words
    tokens = word_tokenize(text.lower())

    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

# Example usage
chatlog = [
    "Hello! How can I assist you today?",
    "I need help with my account. Can you guide me?",
    "Sure! What seems to be the problem?"
]

preprocessed_chatlog = [preprocess_text(message) for message in chatlog]

# Print preprocessed chatlog
for message in preprocessed_chatlog:
    print(message)
