import random


def listSort(rlist):
    k = 0
    
    for k in range(len(rlist)):
        
        for j in range( k+1,len(rlist)):
            if rlist[j] < rlist[k]:
                rlist[k], rlist[j] = rlist[j], rlist[k]
            else:
                rlist[k] = rlist[k]
                   
    return rlist


def median(rlist):
    listSort(rlist)
    m = len(rlist) // 2
    median = rlist[m]
    return median


def mean(rlist):
    acc = 0
    for a in range(len(rlist)):
        acc = acc + rlist[a]

    mean = acc / len(rlist)
    return mean



def mode(rlist):
    adict = {}
    blist=[]

    for i in range(1,101):
        blist.append(i)
    

    for ch in rlist:
        for ch in blist:
             
          
        
          adict[ch] = rlist.count(ch)
    
    print(max(adict, key= adict.get))
    return adict
    

        
      

    

def main():
    
    rlist = []
    
    for i in range (100):
       
       rlist.append(random.randint(1,100)) 
        
    print(rlist)
    print(listSort(rlist))
    print(mean(rlist))
    print(median(rlist))
    print(mode(rlist))
    
    
main()