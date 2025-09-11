word_stat={}
import json
count=1
with open("c://data//country2.txt","r") as f:
    for line in f:
        '''puts the line splitted as a list called my_words'''
        my_words = line.split(' ')
        for words in my_words:
            if words in word_stat:
                '''it adds 1 to the value of the key i.e words'''
                word_stat[words]+=1
            else:
                '''if the word is not in word_stat it makes the value of key 1'''
                word_stat[words]=count
'''with open("c://data//country2.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stat:
          word_stat[word]+=1
        else:
          word_stat[word] = 1'''
print(word_stat)
word_occurences=list(word_stat.values())
max_count=max(word_occurences)
print("The maximum of any word in that poem is",max_count)
for key,value in word_stat.items():
    if value==max_count:
        print("the word with the highest occurrence is",key.upper())








