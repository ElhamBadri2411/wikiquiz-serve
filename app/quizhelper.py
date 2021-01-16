import wikipedia as wiki
from typing import List, Dict
from constants import BLANK
from sklearn.feature_extraction.text import TfidfVectorizer

def top_terms(wiki_data: str):
    vectorizer = TfidfVectorizer()
    response = vectorizer.fit_transform([wiki_data])
    return response


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

def create_question(name_of_wiki_page: str) -> Dict[]:
    pass
    



if __name__ == "__main__":
   print(get_data('Donkey'))
   print (find_usable_sentences(['AB','ac','ad','bb','dd'], 'a'))
   print(remove_special_word('a',  ['AB','ac','ad']))
   print(top_terms(get_data('Donkey')))
    