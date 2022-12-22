import time

def main():
    t0 = time.time()
    array = [1,2,3,4,5,6,7,8,9,10]
    tar = -2
    binary_search(array,tar,10,1)
    t1 = time.time()
    total = t1-t0
    print(f"Time: {total}")

def binary_search(arr, target, high, low) ->int:
    mid = int((high+low)/2)
    if high < low:
        print(-1)
    elif target == mid:
        print(mid)
    elif target > mid:
        low = mid+1
        binary_search(arr,target,high,low)
    elif target < mid:
        high = mid-1
        binary_search(arr,target,high,low)

main()