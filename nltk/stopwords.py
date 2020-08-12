## 불용어 확인
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

english_stopwords = stopwords.words('english')
print(len(english_stopwords))
print(english_stopwords[:10])


## 불용어 제거
from nltk.corpus import stopwords
from nltk import WordPunctTokenizer


text = "Hello, world. These are NLP tutorials."
stop_words = set(stopwords.words('english'))

words = WordPunctTokenizer().tokenize(text)

result = []
for word in words:
    if word not in stop_words:
        result.append(word)

print(words)
print(result)
