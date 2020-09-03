'''
a 10 digit phone number that starts with a +1 that is not part of the 10 and
divided into 3's but the last section is 4 numbers
'''
#random 10 digits
#always begin with +1


import random
import sys


def space(do):
    a=3
    doL = []
    for j in range(0,len(do),a):

        doL.append(do[j:j+a])
    print(doL)
    num = '-'.join(doL)
    no = '+1'
    fin = no + ' ' + num
    return fin





def main():
    for j in range(30):
        do = str()
        for i in range(10):
            do += str(random.randint(0,9))
            


        print(do)
        print(space(do)) 
    
main()   
    


