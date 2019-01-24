'''
    Location extraction file.
    This file extracts the possible crime location for any given crime article.
'''
import CityList
import nltk
import regex as re
import CrimeCheck
# import ArticleSimilarityCheck
import numpy as np
import svo
from nltk.corpus import wordnet 
from copy import deepcopy

## Some important variables used in this program.
CITY_LIST = CityList.ReturnListFromFile()
# print(CITY_LIST)
for i in range(len(CITY_LIST)):
    
    if '\t' in CITY_LIST[i]:
        CITY_LIST[i] = CITY_LIST[i].replace('\t', ' ')

    if '(' in CITY_LIST[i]:

        item = CITY_LIST[i]
        index1 = CITY_LIST[i].find('(')
        index2 = CITY_LIST[i].find(')')
        CITY_LIST[i] = CITY_LIST[i][0:index1-2]
        CITY_LIST.append(item[index1+1:index2])

    if '[' in CITY_LIST[i]:

        item = CITY_LIST[i]
        index1 = CITY_LIST[i].find('[')
        index2 = CITY_LIST[i].find(']')
        CITY_LIST[i] = CITY_LIST[i][0:index1-2]
        CITY_LIST.append(item[index1+1:index2])




# print(CITY_LIST)

PREPOSITION_LIST = ['in','near','from','around','at','outer','south','east','west','north']

LOCATION_TAGS = ['bhavan','pradesh','ashram','nagar','pur','vihar','chowk','road','area','sector','north','east','west','south','garden','park','camp','central','crossing','garh','ganj', 'bad']

PORTER = nltk.PorterStemmer()

# CRIME_WORD_LIST = ['murder','rape', 'bullying','burglary','theft','fraud','harass','hijack','kidnap','kill','robbery','snatching','lynching','shoot']
# crime_list = deepcopy(CRIME_WORD_LIST)
# for crime_word in crime_list:

#     synonyms = wordnet.synsets(crime_word)
#     # print("\n", crime_word, ": ")
#     for syn in synonyms:
#         for i in syn.lemmas():
#             # print(i.name())
#             CRIME_WORD_LIST.append(i.name())

# CRIME_WORD_LIST = list(set(CRIME_WORD_LIST))
# # print(CRIME_WORD_LIST)
CRIME_WORD_STEM_LIST = CrimeCheck.return_stem_list()









'''
    The function returns the entities from the News Article.
    The entities consist following things:
        Names of the people involved in the news.
        Crime Locations.
        Non-Crime Locations.
        Crime word list - Crimes involved.
'''
def return_entities(Text):


    Locations = []
    Entities = []
    crime_word_list = []
    names = []

    sentences = nltk.sent_tokenize(line)
    
    '''
        Entities Extraction.....
    '''
    for sent in sentences:
        # print(sent, "\n")
        words = nltk.word_tokenize(sent.lower())
        for word in words:
            if PORTER.stem(word) in CRIME_WORD_STEM_LIST:
                crime_word_list.append(word)

        chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))
        # print(chunks[0], chunks[1])
        length = len(chunks)
        for i in range(length):
            curr = chunks[i]
            if i == 0:
                prev = None
                Next = chunks[i+1]

            elif i == length-1:
                prev = chunks[i-1]
                Next = None

            else:
                prev = chunks[i-1]
                Next = chunks[i+1]

            if curr and hasattr(curr, 'label') and curr.label() in ['GPE', 'PERSON', 'LOCATION']:
                # print(curr)
                # print(Next)
                if prev and Next and hasattr(prev, 'label') and hasattr(Next, 'label'):# and prev.label() in ['GPE', 'PERSON', 'LOCATION'] and Next.label() in ['GPE', 'PERSON', 'LOCATION']:
                    item = ' '.join(c[0] for c in prev) + ' ' + ' '.join(c[0] for c in curr) + ' ' + ' '.join(c[0] for c in Next)
                    # print(item)
                    Entities.append(item)

                elif prev and hasattr(prev, 'label'):# and prev.label() in ['GPE', 'PERSON', 'LOCATION']:
                    item = ' '.join(c[0] for c in prev) + ' ' + ' '.join(c[0] for c in curr)
                    # print(item)
                    Entities.append(item)

                elif Next and hasattr(Next, 'label'):# and Next.label() in ['GPE', 'PERSON', 'LOCATION']:
                    item = ' '.join(c[0] for c in curr) + ' ' + ' '.join(c[0] for c in Next)
                    # print(item)
                    Entities.append(item)

                else:
                    item = ' '.join(c[0] for c in curr)
                    # print(item)
                    Entities.append(item)
    

    '''
        Location Extraction from these Entities.....
    '''
    for entity in set(Entities):
        
        if entity.lower() in CITY_LIST:
            Locations.append(entity)
            continue


        for loc_tag in LOCATION_TAGS:
            
            if loc_tag in entity:
                Locations.append(entity)
                break

    '''To Print entites'''
    # for location in Locations:
    #     print(location)

    '''
        Names Extraction from Entities.....
    '''
    for name in set(Entities):
        if name not in Locations:
            names.append(name)

    # for name in names:
    #     print(name)

    # print("\nCrime Word: \n")
    # for crime_word in set(crime_word_list):
    #     print(crime_word)


    '''
        Crime Location Segregation.
    '''
    Locations_copy = deepcopy(Locations)
    Crime_Locations = []
    Non_Crime_Locations = []

    sentences = nltk.sent_tokenize(line)
    length = len(sentences)
    for i in range(length):
        curr = sentences[i].lower()
        if i == 0:
            prev = None
            Next = sentences[i+1].lower()
        elif i == length-1:
            prev = sentences[i-1].lower()
            Next = None
        else:
            prev = sentences[i-1].lower()
            Next = sentences[i+1].lower()

        flag = False
        for location in Locations_copy:
            if location in curr:
                for crime_word in crime_word_list:
                    if prev and Next:
                        if crime_word in curr or crime_word in prev or crime_word in Next:
                            Crime_Locations.append(location)

                    elif prev:
                        if crime_word in curr or crime_word in prev:
                            Crime_Locations.append(location)

                    elif Next:
                        if crime_word in curr or crime_word in Next:
                            Crime_Locations.append(location)

                    else:
                        if crime_word in curr:
                            Crime_Locations.append(location)

        
        # Crime_Locations = list(set(Crime_Locations))
        for crime_loc in Crime_Locations:
            # print(crime_loc)
            if crime_loc in Locations_copy:
                Locations_copy.remove(crime_loc)


    '''
        Non-Crime Locations Segregation.....
    '''
    for location in Locations:
        if location not in Crime_Locations:
            Non_Crime_Locations.append(location)

    # print("\nNon-Crime Locations: \n")
    # for location in set(Non_Crime_Locations):
    #     print(location)

    # print("\nCrime Locations: \n")
    # for crime_loc in set(Crime_Locations):
    #     print(crime_loc)

    return names, Non_Crime_Locations, Crime_Locations, crime_word_list


'''
    NewsArticle Class to store Each Article details.....
'''
class NewsArticle():
    """docstring for NewsArticle"""
    def __init__(self, Names, Non_Crime_Locations, Crime_Locations, Crime_list, text):
        
        self.Names = Names
        self.Non_Crime_Locations = Non_Crime_Locations
        self.Crime_Locations = Crime_Locations
        self.Crime_list = Crime_list
        self.text = text


    def return_entities(self):

        return self.Names, self.Non_Crime_Locations, self.Crime_Locations, self.Crime_list


    def print(self):
        
        print("\nName: ")
        for name in set(self.Names):
            print(name)

        print("\nNon-Crime Locations: ")
        for ncl in set(self.Non_Crime_Locations):
            print(ncl)

        print("\nCrime Locations: ")
        for cl in set(self.Crime_Locations):
            print(cl)

        print("\nCrime Word List: ")
        for cwl in set(self.Crime_list):
            print(cwl)

        print("\nArticle Text: ")
        print(self.text)          
        


    def return_text(self):

        return self.text


    def return_names(self):

        return self.Names

if __name__ == "__main__":

    NewsArticles = []
    with open("file.txt", 'r') as file:
        for line in file:
            line1 = file.readline()
            line = line.strip() + ". " + line1.strip()
            Names, NCL, CL, CWL = return_entities(line)

            news_article = NewsArticle(Names, NCL, CL, CWL,line)
            NewsArticles.append(news_article)
            
    i=1
    for news_article in NewsArticles:
        print("News: ", i)
        i+=1
        news_article.print()



    # for news_article in NewsArticles:

    #     # for line in file:
    #     # line1 = file.readline()
    #     document = news_article.return_text()
    #     print(document)
    #     subjects = news_article.return_names() # svo.extract_subject(document)
    #     subjects = [sub.lower() for sub in subjects]
    #     sentences = nltk.sent_tokenize(document)
    #     list_of_svo = []
    #     object = []
    #     list_of_svo_sentences = []
    #     for sub in subjects:
    #             # print("present subject:", sub)
    #             tagged_sents = svo.tag_sentences(sub, document)
    #             # print(tagged_sents)
    #             svos = [svo.get_svo(sentence, sub) for sentence in tagged_sents]
    #             for svo_entry in svos:
    #                 if svo_entry:
    #                     list_of_svo.append(svo_entry)
    #                     # if porter.stem(svo['action'].lower()) not in action:
    #                     #     action.append(porter.stem(svo['action'].lower()))
    #                     object.append(svo_entry['object'])
    #                     phrase = " ".join(item[0] for item in svo_entry['phrase'])
    #                     list_of_svo_sentences.append(phrase)

    #     for lsvo in list_of_svo:
    #         # if lsvo['action'].lower() in CRIME_WORD_STEM_LIST:

    #             # print("\nsvo: ", i)
    #         print("Subject: ", lsvo['subject'])
    #         print("Action: ", lsvo['action'])
    #         print("Object: ", lsvo['object'])


# from vocabulary.vocabulary import Vocabulary as vb
# print(vb.synonym("lynching"))

            # for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            #     print(chunk)
            # print("\n\n")


        # ret = getNGrams(line, 4)
        # print(ret)
        # location = []
        # ret = nltk.ngrams(line.split(), 5)
        # for i in ret:
        #     chunk = nltk.ne_chunk(nltk.pos_tag(i))
        #     for ch in chunk:
        #         if hasattr(ch, 'label'):
        #             if ch.label() == 'PERSON' or ch.label() == 'GPE' or ch.label() == 'LOCATION':
        #                 location.append(' '.join(c[0] for c in ch))

        # p = list(set(location))

        # for i in p:
        #     print(i)
        # loca = []
        # for i in p:
        #     for j in p:
        #         i_words = i.split()
        #         j_words = j.split()
        #         if len(i_words) > len(j_words):

        #             count = 0
        #             for word in j_words:
        #                 if word in i_words:
        #                     count+=1
        #                     if count > 1:
        #                         loca.append(i)
        #                         break

        #         else:
        #             count = 0
        #             for word in j_words:
        #                 if word in i_words:
        #                     count+=1
        #                     if count > 1:
        #                         loca.append(j)
        #                         break                    


        # # for item in set(loca):
        # #     print(item)

        # loc = []

        # for i in loca:
        #     for j in loca:
                
        #         i_words = i.split()
        #         j_words = j.split()

        #         if i_words[-1] == j_words[0]:
                    
        #             total = i_words + j_words[1:]

        #             loc.append(' '.join(word for word in total))

        #         elif i_words[0] == j_words[-1]:

        #             total = j_words + i_words[1:]

        #             loc.append(' '.join(word for word in total))

        #         else:
        #             loc.append(i)
        #             loc.append(j)

        # for item in set(loc):
        #     print(item)
