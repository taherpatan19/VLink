def isPrime():
    num=int(input("Enter a Even num: "))
    if num>=10:
        if (num%2)==0 :

            for i in range(2,num//2):
                if (num%i)==0:
                    print(num)
                    break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    isPrime()

    