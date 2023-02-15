import nltk
from typing import List, Tuple
import string
from nltk.stem.porter import PorterStemmer
from gensim import corpora
import spacy
nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')
nltk.download('stopwords')


# class Preprocessing():
#     def __init__(self):
#         self.sentences = 

def preprocessing(path="data/input.txt"):
    sentencesList = file2sentences(path)
    lower_sentencesList = lower(sentences=sentencesList)
    words_list = tokenize(sentences=lower_sentencesList)
    normalized_words_list = eliminateStopWords(words_list=words_list)
    for lst in normalized_words_list:
        lst = stemming(words=lst)
    dic = corpus(words_list=normalized_words_list)
    return list(dic.keys())

def file2sentences(path):
    path="data/input.txt"
    f = open(path, "r")
    str = ""
    for l in f:
        str += l
    sentences = str.split('.')
    return sentences

def lower(sentences: List[str]):
    lower_sentences: List[str] = list(
        sentence.lower() for sentence in sentences
    )
    return lower_sentences
    
def tokenize(sentences: List[str]):
    # words_list: List[List[str]] = list(
    #     nltk.tokenize.word_tokenize(sentence) for sentence in sentences
    # )
    words_list = []
    for s in sentences:
        lst = []
        # s = "The oxDNA model of Deoxyribonucleic acid has been applied widely to systems in biology."
        doc = nlp(s)
        for d in doc:
            token = d
            lst.append(token.lemma_)
        words_list.append(lst)

    return words_list

def eliminateStopWords(words_list: List[List[str]]):
    stopwords: List[str] = nltk.corpus.stopwords.words('english')
    exclude_words: List[str] = list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)
    needless_words = stopwords + exclude_words

    needless_words.append('—')
    needless_words.append('\n')
    needless_words.append('’s')

    normalized_words_list: List[List[str]] = list(
        list(word for word in words if word not in needless_words) for words in words_list
    )

    return normalized_words_list

def stemming(words: List[str]):
    ps: PorterStemmer = PorterStemmer()
    stemmed_words: List[str] = list(ps.stem(word) for word in words)
    return stemmed_words


def corpus(words_list: List[List[str]]):
    dictionary: corpora.Dictionary = corpora.Dictionary(words_list)
    # print(dictionary.token2id)
    # -> {'a': 0, 'and': 1, 'blue': 2, 'have': 3, 'i': 4, 'pen': 5, 'red': 6, 'like': 7, 'you': 8}

    corpus: List[List[Tuple[int, int]]] = list(map(dictionary.doc2bow, words_list)) # ベクトル化
    # print(corpus)
    # -> [[(0, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 2), (6, 1)], [(6, 1), (7, 1), (8, 1)]]

    return dictionary.token2id

def be_lemma():
    sent = "The oxDNA model of Deoxyribonucleic acid has been applied widely to systems in biology."
    doc = nlp(sent)

    print(doc[2])

    for d in doc:
      token = d
      print(d, ' .lemma_:  ', token.lemma_, type(token.lemma_), sep='\t')


def main():
    # lower()
    # tokenize()
    # eliminateStopWords()
    # stemming()
    # corpus()

    lst = preprocessing()
    print(lst)
    
if __name__ == '__main__':
    main()

