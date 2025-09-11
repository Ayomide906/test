from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def reverse_string(self,word):
        """split word into list"""
        word_list=word.split()
        for words in word_list:
            #splits the letters in the word into a list then add a space
            a=list(words +' ')
            b=a[::-1] #flips the list created
            c=''.join(b) #joins the list into a string
            self.container.appendleft(c)
        return ''.join(self.container)
class Queue:
    def __init__(self):
        self.container=[]
s=Stack()
if __name__=='__main__':
    P = s.reverse_string("We will conquere COVID-19")
    print(P)
