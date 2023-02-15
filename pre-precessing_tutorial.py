import nltk
from typing import List, Tuple
import string
from nltk.stem.porter import PorterStemmer
from gensim import corpora
nltk.download('punkt')
nltk.download('stopwords')

def lower():
    sentences: List[str] = ['I  have  a pen', 'That  is a window']
    print(sentences)
    # -> ['I  have  a pen', 'That  is a window']

    lower_sentences: List[str] = list(
        sentence.lower() for sentence in sentences
    )
    print(lower_sentences)
    # -> ['i  have  a pen', 'that  is a window']

def tokenize():
    sentences: List[str] = ['i  have  a pen', 'that  is a window']
    print(sentences)
    # -> ['i  have  a pen', 'that  is a window']

    words_list: List[List[str]] = list(
        nltk.tokenize.word_tokenize(sentence) for sentence in sentences
    )
    print(words_list)
    # -> [['i', 'have', 'a', 'pen'], ['that', 'is', 'a', 'window']]

def eliminateStopWords():
    words_list: List[List[str]] = [['i', 'have', 'a', 'pen'], ['that', 'is', 'a', 'window']]
    stopwords: List[str] = nltk.corpus.stopwords.words('english')
    print(stopwords)
    # -> ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', ...（省略）]

    normalized_words_list: List[List[str]] = list(
        list(word for word in words if word not in stopwords) for words in words_list
    )
    print(normalized_words_list)

    exclude_words: List[str] = list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)
    print(exclude_words)

def stemming():
    ps: PorterStemmer = PorterStemmer()
    words: List[str] = ['mechanical', 'pencil', 'go', 'went', 'goes', 'pencils']
    print(words)
    # -> ['mechanical', 'pencil', 'go', 'went', 'goes', 'pencils']

    stemmed_words: List[str] = list(ps.stem(word) for word in words)
    print(stemmed_words)
    # -> ['mechan', 'pencil', 'go', 'went', 'goe', 'pencil']

def corpus():
    words_list: List[List[str]] = [['i', 'have', 'a', 'red', 'pen', 'and', 'a', 'blue', 'pen'], ['you', 'like', 'red']]
    print(words_list)
    # -> [['i', 'have', 'a', 'red', 'pen', 'and', 'a', 'blue', 'pen'], ['you', 'like', 'red']]

    dictionary: corpora.Dictionary = corpora.Dictionary(words_list)
    print(dictionary.token2id)
    # -> {'a': 0, 'and': 1, 'blue': 2, 'have': 3, 'i': 4, 'pen': 5, 'red': 6, 'like': 7, 'you': 8}

    corpus: List[List[Tuple[int, int]]] = list(map(dictionary.doc2bow, words_list)) # ベクトル化
    print(corpus)
    # -> [[(0, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 2), (6, 1)], [(6, 1), (7, 1), (8, 1)]]

def main():
    lower()
    tokenize()
    eliminateStopWords()
    stemming()
    corpus()
    
if __name__ == '__main__':
    main()

