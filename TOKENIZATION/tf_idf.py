import pandas as pd
messages=pd.read_csv('C:\MyCode\PythonLearning\smaple.csv',
                    sep='\t',names=["label","message"])
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
wordlemmatize=WordNetLemmatizer()

corpus=[]

for i in range(0,len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review=review.lower()
    review=review.split()
    review=[wordlemmatize.lemmatize(word) for word in review if word not in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

#print(corpus)

from sklearn.feature_extraction.text import TfidfVectorizer

'''
tf=TfidfVectorizer(max_features=100)
x=tf.fit_transform(corpus).toarray()
print(x)
'''
tf=TfidfVectorizer(max_features=100,ngram_range=(2,2))
x=tf.fit_transform(corpus).toarray()
print(tf.vocabulary_)