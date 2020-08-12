import nltk
from nltk import WordPunctTokenizer

nltk.download('punkt')

text = "Hello, world. These are NLP tutorials."
print(WordPunctTokenizer().tokenize(text))
