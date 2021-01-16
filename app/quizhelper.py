import wikipedia as wiki
from typing import List, Dict
from app.constants import BLANK, QUESTION, ANSWER, OPTIONS 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def get_tfidf(wiki_data: List[str]):
    """Returns top 5 tfidf words ranked from highest to lowest in a dictionary"""

    vectorizer = TfidfVectorizer(use_idf=True)
    tfIdf = vectorizer.fit_transform(wiki_data)
    print(tfIdf)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=vectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    df = df.nlargest(5, 'TF-IDF')
    tfidflist = list(df.index.values)

    return tfidflist
    
    
def get_data(name_of_wiki_page: str) -> List[str]:
    """Returns the data from wikipedia page name_of_wiki_page, with each index in the list being a sentence 
    """

    all_data = wiki.page(name_of_wiki_page, auto_suggest=False).content
    split_data = all_data.split('.')

    return split_data

def find_usable_sentences(wikipedia_page: List[str], special_word: str) -> List[str]:
    """returns a list of usable sentences using the information recieved from a wikipedia page, 
    finds all usable sentences that have special_word in it

    >>> find_usable_sentences(['AB','ac','ad','bb','dd'], 'a')
    ['AB','ac','ad']
    """

    possible_sentences = []

    for sentence in wikipedia_page:
        if special_word.lower() in sentence.lower():
            possible_sentences.append(sentence)

    possible_sentences.sort()
    return possible_sentences

def remove_special_word(special_word: str, possible_sentences: List[str]) -> List[str]:
    """ Returns possible_sentences with special_word removed from every index,
    replaced by BLANK"""

    sentences_with_blank = []
    for sentence in possible_sentences:
        blanked_sentence = sentence.lower().replace(special_word, BLANK)
        sentences_with_blank.append(blanked_sentence)
    
    return sentences_with_blank

def create_question(name_of_wiki_page: str):
    pass
    

if __name__ == "__main__":
   print (find_usable_sentences(['AB','ac','ad','bb','dd'], 'a'))
   print(remove_special_word('a',  ['AB','ac','ad']))
   print(get_tfidf(get_data('Donkey')))
    