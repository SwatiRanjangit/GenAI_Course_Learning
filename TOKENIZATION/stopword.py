'''
stopwords are those words which does not play important role in any type of classification or text processing for example in a paragraph
there might be many words like: is, of,the,their,why,this ,he,she, and so on so these words are not that much importnat when comes to any classification
or spam so we need to remove those words to focus on important words so it is used by stopwords in nltk
'''
corpus='''
I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards, the Greeks, the Turks, the Mughals, the Portuguese, the British, the French, the Dutch – all of them came and looted us, took what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history, and tried to enforce our way of life on them. Why? Because we respect the freedom of others.

That is why my first vision is that of freedom. I believe that India got its first vision of this freedom in 1857, when we started the war of independence. It is this freedom that we must protect and nurture. If we are not free, no one will respect us.

My second vision for India is development. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among the top 5 nations of the world in terms of GDP. We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognized today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?

I have a third vision. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand.

I am reminded of a conversation between Dr. Sarvapalli Radhakrishnan and his students. When asked what makes a nation truly great, he said, “A great nation is built by great minds, by great character and by great discipline.” India needs these qualities today, more than ever.

Why is the media here so negative? Why are we so embarrassed to recognize our own strengths, our achievements? We are the first nation to reach Mars in our maiden attempt. We have built one of the largest IT industries in the world. Our scientists have made major contributions to fields like space, medicine, and atomic energy. Still, we constantly compare ourselves with others and doubt our potential.

'''

'''
from nltk.stem import SnowballStemmer
import nltk
from nltk.corpus import stopwords
#print(stopwords.words('english'))
stemmer = SnowballStemmer('english')

# tokenize (paragraph to sentences)
#print(nltk.sent_tokenize(corpus))
sentences=nltk.sent_tokenize(corpus)

#travese whole sentence and which word is not in stopwords only take those and do stemming.

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) # convet all list word in sentenctes
    
print(sentences)
'''

#using lemmatiation

from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
#print(stopwords.words('english'))
lemmitizer = WordNetLemmatizer()

# tokenize (paragraph to sentences)
#print(nltk.sent_tokenize(corpus))
sentences=nltk.sent_tokenize(corpus)

#travese whole sentence and which word is not in stopwords only take those and do stemming.

for i in range(len(sentences)):
    #sentences[i]=sentences[i].tolower()
    words=nltk.word_tokenize(sentences[i])
    words=[lemmitizer.lemmatize(word.lower(),'v') for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) # convet all list word in sentenctes
    
print(sentences)

