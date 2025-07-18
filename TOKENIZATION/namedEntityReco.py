sentence='The eiffel tower was vuilt from 1887 by french engineer Gustahq.'

import nltk
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
words = nltk.word_tokenize(sentence)
tag_ele = nltk.pos_tag(words)
named_entity = nltk.ne_chunk(tag_ele)
print(named_entity.draw())

#print(tag_ele)
