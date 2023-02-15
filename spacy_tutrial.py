import spacy
nlp = spacy.load('en_core_web_sm')

sent = "I don't like apple."
doc = nlp(sent)

print(doc[2])

# 3番目のトークン
token = doc[2]
print('.text:    ', token.text, type(token.text), sep='\t')
print('.lemma_:  ', token.lemma_, type(token.lemma_), sep='\t')
print('.pos_:    ', token.pos_, type(token.pos_), sep='\t')
print('.tag_:    ', token.tag_, type(token.tag_), sep='\t')
print('.dep_:    ', token.dep_, type(token.dep_), sep='\t')
print('.shape:   ', token.shape_, type(token.shape_), sep='\t')
print('.is_alpha:', token.is_alpha, type(token.is_alpha), sep='\t')
print('.is_stop: ', token.is_stop, type(token.is_stop), sep='\t')
'''
出力:
.text:          n't     <class 'str'>
.lemma_:        not     <class 'str'>
.pos_:          ADV     <class 'str'>
.tag_:          RB      <class 'str'>
.dep_:          neg     <class 'str'>
.shape:         x'x     <class 'str'>
.is_alpha:      False   <class 'bool'>
.is_stop:       False   <class 'bool'>
'''
