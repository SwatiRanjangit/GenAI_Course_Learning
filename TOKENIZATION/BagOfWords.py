import pandas as pd

message=pd.read_csv('C:\MyCode\PythonLearning\smaple.csv',sep='\t',names=['lable','message'])
#print(message)

# data preprocessing and cleaning

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer
corpus=[]
ps=PorterStemmer()

for i in range(0,len(message)):
    review=re.sub('[^a-zA-Z]',' ',message['message'][i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)
    
#print(corpus)


#create bag of words model

from sklearn.feature_extraction.text import CountVectorizer

#for normal BOW
#cv=CountVectorizer(max_features=100)

# for binary BOW
cv=CountVectorizer(max_features=100,binary=True)
x = cv.fit_transform(corpus).toarray()
print(x)



# BOW By using lemmatization
#lemmatizer = WordNetLemmatizer()
#corpus = []

#from sklearn.feature_extraction.text import CountVectorizer
'''
#for normal BOW
cv=CountVectorizer(max_features=100)
for i in range(len(message)):
    msg = message['message'][i]
    msg = re.sub('[^a-zA-Z]', ' ', msg)
    msg = msg.lower()
    tokens = nltk.word_tokenize(msg)
    words = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
    cleaned = ' '.join(words)
    corpus.append(cleaned)


print("Cleaned Corpus:")
for line in corpus:
    print(line)
'''
 
# for binary BOW
cv=CountVectorizer(max_features=100,binary=True)
x = cv.fit_transform(corpus).toarray()
#print(x)


# create Bag of word with N-Gram
#from sklearn.feature_extraction.text import CountVectorizer

#for binary BOW
cv = CountVectorizer(max_features=50,binary=True,ngram_range=(1,2)) #bigram

print(cv.vocabulary_)