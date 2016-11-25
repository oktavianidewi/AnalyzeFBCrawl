from nltk.corpus import wordnet

list1 = ['Compare', 'require']
list2 = ['choose', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list = []

for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1)
        wordFromList2 = wordnet.synsets(word2)
        print 'synset dari wordlist1', wordFromList1
        print 'synset dari wordlist2', wordFromList2

        if wordFromList1 and wordFromList2: #Thanks to @alexis' note
            s = wordFromList1[0].wup_similarity(wordFromList2[0])
            list.append(s)

print(list)
print len(list)
print len(list2)
