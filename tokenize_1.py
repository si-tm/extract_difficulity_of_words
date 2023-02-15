import spacy
nlp = spacy.load('en_core_web_sm')

def main():

    sent = "The oxDNA model of Deoxyribonucleic acid has been applied widely to systems in biology."
    doc = nlp(sent)

    print(doc[2])

    for d in doc:
      token = d
      print(d, ' .lemma_:  ', token.lemma_, type(token.lemma_), sep='\t')

if __name__ == '__main__':
  main()
