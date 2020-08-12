from nltk import WordPunctTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

text = "Hello, world. These are NLP tutorials."
words = WordPunctTokenizer().tokenize(text)
print(words)

porter_stemmer = PorterStemmer()
print([porter_stemmer.stem(w) for w in words])

lancaster_stemmer = LancasterStemmer()
print([lancaster_stemmer.stem(w) for w in words])
