#This algorithms is very slow average is O((n+1)!)
#with a array of just a length of 10 it took 157 seconds and half a million iterations
import time
from random import shuffle

def main():
    t0 = time.time()
    l = [5,6,3,2,1,2,3,5,6,9]
    print(bogo_sort(l))
    t1 = time.time()
    total = t1-t0
    print(total)



def sorted(data) -> bool:
    return all (a <= b for a, b in zip(data, data[1:]))

def bogo_sort(list):
    x=0
    while not sorted(list):
        x+=1
        print(x)
        shuffle(list)
    return list

main()