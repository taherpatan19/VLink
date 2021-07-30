def minChar():
    n=int(input("Enter lenght of password: "))
    passw=input()
    hasLower = 0

    hasUpper = 0

    hasDigit = 0

    specialChar = 0

    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

     

    for i in range(n):

        if passw[i].islower():

            hasLower+=1

        if passw[i].isupper():

            hasUpper+=1

        if passw[i].isdigit():  

            hasDigit+=1

        if passw[i] not in normalChars:

            specialChar+=1 

    print("Password contains :")
    print("Special Character", specialChar)
    print("Digits", hasDigit)
    print("Uppercase", hasUpper)
    print("Lowercase",hasLower)
    sum=hasLower+hasUpper+hasDigit+specialChar
    if sum<8:
        print((8 - sum)," more characters to be added.")
    else:
        print(passw) 

if __name__ == "__main__":
    minChar()

