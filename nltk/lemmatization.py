import nltk
from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

text = "Hello, world. These are NLP tutorials."
words = WordPunctTokenizer().tokenize(text)

lemmatizer = WordNetLemmatizer()

print(words)
print([lemmatizer.lemmatize(w) for w in words])
