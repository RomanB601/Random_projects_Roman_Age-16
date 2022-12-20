def main():
    num = int(input("What is the number?"))
    prime(num)

def prime(x):
    if x > 1:
        if x % 2 == 0: 
            print(f"Your {x} is a prime number")
        else: print(f"{x} is not a prime number")
    else: print(f"{x} is not a prime number")
            

main()