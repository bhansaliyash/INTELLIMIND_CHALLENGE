import nltk

#Enter the file name 
text = open('yourfile.txt').read().replace('\n', '')

sentences=nltk.sent_tokenize(text) #Text is broken into sentences
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences] #Words are extracted from the sentences

tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences] #Giving tags based on Parts Of Speech
chunked_sents = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]#Get the nested tree object to determine the NamedEntities
named_entities = []

#Extracting the named entities based on the tags
for ne_tagged in chunked_sents:
    for tagged_tree in ne_tagged:
        if hasattr(tagged_tree, 'label'):
                entity = ' '.join(c[0] for c in tagged_tree.leaves())
                named_entities.append(entity)
                
named_entities = list(set(named_entities))
print named_entities