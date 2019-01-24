import nltk
from copy import deepcopy
from nltk.corpus import wordnet 

POS_TAG_LIST = ['$','',',','(',')','--','.',':','CC','CD','DT','EX','IN','MD','PDT','POS','PRP','PRP$','SYM','TO','WDT','WP','WP$','WRB','``','NNP','NNPS','RB','RBR','RBS','RP']

PORTER = nltk.PorterStemmer()

def return_stem_list():
    CRIME_WORD_LIST = ['murder','rape', 'bullying','burglary','theft','fraud','harass','hijack','kidnap','kill','robbery','snatching','lynching','shoot']
    crime_list = deepcopy(CRIME_WORD_LIST)
    for crime_word in crime_list:

        synonyms = wordnet.synsets(crime_word)
        # print("\n", crime_word, ": ")
        for syn in synonyms:
            for i in syn.lemmas():
                # print(i.name())
                CRIME_WORD_LIST.append(i.name())

    CRIME_WORD_LIST = list(set(CRIME_WORD_LIST))
    # print(CRIME_WORD_LIST)
    CRIME_WORD_STEM_LIST = [PORTER.stem(crime_word) for crime_word in CRIME_WORD_LIST]
    return CRIME_WORD_STEM_LIST

def crime_article_check(article):
    article = article.replace(","," ")
    sentences = article.split(".")

    words = []

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            words.append(token)

    StemWord = [PORTER.stem(word) for word in words]

    for word in CRIME_WORD_STEM_LIST:
        if word in StemWord:
            print(word)
            return True

    return False

def return_crime_word_list(article):
    article = article.replace(","," ")
    sentences = article.split(".")

    words = []
    crime_list = []

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            words.append(token)

    StemWord = [PORTER.stem(word) for word in words]

    for word in CRIME_WORD_STEM_LIST:
        if word in StemWord:
            crime_list.append(word)

    return crime_list
