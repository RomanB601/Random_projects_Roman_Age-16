#This project is creating a selection sort method Worst case scenario O(n^2)
import time

def main():
    start_time = time.time()
    l = [2,8,5,3,6,1,6,3,7,8,5,4,6,2,7,6,3,8,6,4,5,9,8,7,0,1,2,4,3,5,4,8,7,6,8,5,4,8,5,6,7,9,4,3,5,6,4,5,6,7,8,4,3,2,9,5,2,1,1,5,2,3,]
    selection_sort(l)
    print("--- %s seconds ---" % (time.time() - start_time))

def selection_sort(list):
    for r in range(len(list)):
        for i in range(len(list)):
            min = list[i]
            if list[r] < min:
                list[i] = list[r]
                list[r] = min
    print(list)


main()