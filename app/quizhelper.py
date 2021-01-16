import wikipedia as wiki
from typing import List, Dict
from constants import BLANK, QUESTION, ANSWER, OPTIONS 
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import pandas as pd
from random import choice, shuffle

def get_tfidf(wiki_data: List[str]):
    """Returns top 5 tfidf words ranked from highest to lowest in a dictionary"""

    vectorizer = TfidfVectorizer(use_idf=True, stop_words=set(ENGLISH_STOP_WORDS))
    tfIdf = vectorizer.fit_transform(wiki_data)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=vectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    df = df.nlargest(10, 'TF-IDF')
    tfidflist = list(df.index.values)

    return tfidflist
    
    
def get_data(name_of_wiki_page: str) -> List[str]:
    """Returns the data from wikipedia page name_of_wiki_page, with each index in the list being a sentence 
    """
    print(name_of_wiki_page)
    print(wiki.search(name_of_wiki_page))
    print(wiki.suggest(name_of_wiki_page))

    wiki_search = wiki.search(name_of_wiki_page)
    name_of_wiki_page_caps = name_of_wiki_page.upper()
    wiki_search_caps = [item.upper() for item in wiki_search]

    if name_of_wiki_page_caps in wiki_search_caps:
        print(name_of_wiki_page_caps in wiki_search_caps)
        all_data = wiki.page(name_of_wiki_page, auto_suggest=False).content
    else:
        all_data = wiki.page(wiki.suggest(name_of_wiki_page)).content

    all_data = all_data.replace('\n','')
    all_data = all_data.replace('\t','')
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

def create_questions(name_of_wiki_page: str):
    """Returns a list of questions
    """
    wiki_data = get_data(name_of_wiki_page)
    top_ten = get_tfidf(wiki_data)
    question_list = []

    for key_word in top_ten:

        possible_options = top_ten[:]
        possible_options.remove(key_word)

        possible_sentences = find_usable_sentences(wiki_data, key_word)
        possible_sentences = remove_special_word(key_word, possible_sentences)

        random_question = choice(possible_sentences)

        other_options = []
        for i in range(3):
            option = choice(possible_options)

            other_options.append(option)
            possible_options.remove(option)

        other_options.append(key_word)
        shuffle(other_options)
        question_list.append( {QUESTION: random_question, ANSWER: key_word, OPTIONS: other_options } )
    
    return question_list

if __name__ == "__main__":
   #print(create_questions('whale'))
   print('TYFUMP')
   print(get_data('arpods'))
   