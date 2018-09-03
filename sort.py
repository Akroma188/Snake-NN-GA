#!/usr/bin/env python
import random

class C:
    def __init__(self,count):
        self.count = count

    # def __cmp__(self,other):
    #     return cmp(self.count,other.count)

longList = [C(random.random()) for i in range(10)] #about 6.1 secs
longList2 = longList[:]


longList2.sort(key = lambda pop: pop.count) #about 9 - 6.1 = 3 secs
print(longList2[0].count)
print(longList2[1].count)
print(longList2[2].count)