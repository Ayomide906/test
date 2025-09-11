from collections import deque
dc=deque()
class Father:
    def gardening(self):
        print("I enjoy gardening")
class Mother:
    def cooking(self):
        print("I love cooking")
class child(Father,Mother):#Helps child inherit father and mother methods
    def sport(self):
        print("I enjoy Sports")
c=child()
c.sport()
c.gardening() #basically you can call methods of the father and mother class.
c.cooking()