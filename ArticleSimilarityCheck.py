''' Module to check the similarity of any two articles. '''

## Modules import statements
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import math


def Preprocessing(text):
    '''
        Function for pre-processing of text.
    '''
    eng_stopwords = stopwords.words("english")
    words_in_text = nltk.word_tokenize(text)
    text = [word.lower() for word in words_in_text if word not in eng_stopwords]

    return text


def tf(text, wordset):
    '''
        function to calculate term frequency of given text.
    '''
    freq_text = FreqDist(text)
    text_length = len(text)
    text_tf_dict = dict.fromkeys(wordset, 0)
    for word in text:
        text_tf_dict[word] = freq_text[word]/text_length

    return text_tf_dict


def idf(text1, text2, wordset):
    '''
        Function to calculate inverse document frequency of given text.
    '''
    idf_dict = dict.fromkeys(wordset, 0)
    no_of_docs = 2
    for word in idf_dict.keys():
        if word in text1:
            idf_dict[word] += 1

        if word in text2:
            idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = 1 + math.log(no_of_docs/(float(val)))

    return idf_dict


def tf_idf(text, wordset, tf_dict, idf_dict):
    '''
        function to calculate the tf-idf value for a given documet.
    '''
    text_tf_idf_dict = dict.fromkeys(wordset, 0)
    for word in text:
        text_tf_idf_dict[word] = tf_dict[word] * idf_dict[word]

    return text_tf_idf_dict


def distance_computation(tf_idf1, tf_idf2):
    '''
        function to calculate the distance between two text.
    '''
    v1 = list(tf_idf1.values())
    v2 = list(tf_idf2.values())

    return 1 - nltk.cluster.cosine_distance(v1,v2)


def similarity_score(document1, document2):
    '''
        function to calculate the similarity between given two documents.
    '''

    text1 = Preprocessing(document1)
    text2 = Preprocessing(document2)

    wordset = set(text1).union(set(text2))

    tf1 = tf(text1,wordset)
    tf2 = tf(text2,wordset)

    doc_idf = idf(text1,text2,wordset)

    tf_idf1 = tf_idf(text1,wordset,tf1,doc_idf)
    tf_idf2 = tf_idf(text2,wordset,tf2,doc_idf)

    similarity = distance_computation(tf_idf1, tf_idf2)

    print("Similarity Score: ", similarity)



if __name__ == "__main__":

    document1 = " Thane man whose genitals were chopped off for stalking woman dies. A 27-year-old man from Maharashtra’s Thane district whose private parts were allegedly chopped off by three persons, including a woman he was reportedly stalking, has died in a Mumbai hospital, police said Sunday.  An official said that Tushar Pujare, a home loan adviser, was allegedly stalking a 42-year-old woman in the district’s Manpada area and had also visited her home and told her husband about his infatuation.  Pujare’s brother, in his complaint to the police, said 15 days prior to the incident, the woman had warned Pujare of dire consequences if he did not stop his advances.  On December 25, Pujare was called to Nandivli area of Dombivali by the accused on the pretext of arranging a home loan, the official said.  “Pujare was assaulted there and the woman chopped off his private parts with a knife. The woman rushed Pujare to a nearby hospital and then left from there,” the official said.  Police began their probe after being alerted by hospital authorities and zeroed in on the three, including the woman, on December 26, he said.  “On Friday, at around 11pm, Pujare succumbed to his injuries in JJ Hospital in Byculla in Mumbai. We have added the charge of murder against the three accused,” a senior Manpada police official said Sunday.  The official refused to identify the woman but gave the names of the other two accused as Tejas Mhatre and Pratik Kenia.  First Published: Dec 30, 2018 19:27 IST"
    document2 = "Deputy Of Kashmir's Most Wanted Terrorist Among 6 Killed In J&K's Pulwama. The encounter was launched in Arampora village in Awantipora area in south Kashmir.  Highlights Encounter was launched in Awantipora area in Pulwama district Huge quantity of arms and ammunition have been recovered from the spot Zakir Moosa, one of Kashmir's most wanted, was recently seen in Punjab  Six terrorists, including a close aide of Zakir Musa, one of Jammu and Kashmir's most wanted terrorist, were killed in an encounter with security forces in Pulwama district today. Soliha, also known as Rehaan Khan, was the deputy chief of Zakir Musa's group Ansar Ghazwat-ul Hind, which has links with Al-Qaeda.  Security forces had launched a cordon and search operation in the Awantipora area in the south Kashmir district after they received specific intelligence input about the presence of terrorists there.  Police said as the forces were conducting searches, terrorists fired upon them, triggering the encounter.  \"Weapons and war-like stores have been recovered. The operation is over,\" a Defence Ministry spokesman said.  Zakir Musa is a former Hizbul Mujahideen terrorist, and his Ansar Ghazwat-ul Hind is said to also have links to Jaish-e-Mohammed. He is one of the most wanted terrorists who are currently operating in the Kashmir valley.  In November, Punjab was put on high alert after he was spotted near Amritsar. Posters of Zakir Moosa were put up across the state following inputs that he along with seven members of the terror outfit Jaish-e-Mohammed were believed to be sighted in Ferozepur.  Earlier that month, the Punjab Police arrested two students associated with his terrorist organisation in connection with Maqsudan Police Station hand-grenade blasts case of September 14."
    document3 = " Maharashtra man whose private parts were chopped off for stalking woman, dies - Times of India  THANE: A 27-year-old man from Maharashtra's Thane district whose private parts were allegedly chopped off by three persons, including a woman he was reportedly stalking, has died in a Mumbai hospital, police said on Sunday.An official said that Tushar Pujare , a home loan adviser, was allegedly stalking a 42-year-old woman in the district's Manpada area and had also visited her home and told her husband about his infatuation.Pujare's brother, in his complaint to the police, said 15 days prior to the incident, the woman had warned Pujare of dire consequences if he did not stop his advances.On December 25, Pujare was called to Nandivli area of Dombivali by the accused on the pretext of arranging a home loan, the official said.\"Pujare was assaulted there and the woman chopped off his private parts with a knife. The woman rushed Pujare to a nearby hospital and then left from there,\" the official said.Police began their probe after being alerted by hospital authorities and zeroed in on the three, including the woman, on December 26, he said.\"On Friday, at around 11pm, Pujare succumbed to his injuries in JJ Hospital in Byculla in Mumbai. We have added the charge of murder against the three accused,\" a senior Manpada police official said Sunday.The official refused to identify the woman but gave the names of the other two accused as Tejas Mhatre and Pratik Kenia."
    similarity_score(document1,document2)
    similarity_score(document2,document3)
    similarity_score(document1,document3)


######## Simple model to check ########

# from gensim.models.doc2vec import TaggedDocument
# import gensim

# text1 = Preprocessing(document1)
# text2 = Preprocessing(document2)
# text3 = Preprocessing(document3)

# tagged_docs = []
# doc1 = TaggedDocument(words=text1, tags=[u'NEWS_1'])
# tagged_docs.append(doc1)
# doc2 = TaggedDocument(words=text2, tags=[u'NEWS_2'])
# tagged_docs.append(doc2)

# model = gensim.models.Doc2Vec(tagged_docs, dm=0, alpha=0.025, size=20, min_alpha=0.025, min_count=0)
# for epoc in range(80):
#     if epoc%20 == 0:
#         print("training epoc: ", epoc)

#     model.train(tagged_docs)
#     model.alpha -= .002
#     model.min_alpha = model.alpha

# similarity = model.n_similarity(text1, text2)
# print("Similarity Score: ", similarity*100)

# similarity = model.n_similarity(text2, text3)
# print("Similarity Score: ", similarity*100)

# similarity = model.n_similarity(text1, text3)
# print("Similarity Score: ", similarity*100)