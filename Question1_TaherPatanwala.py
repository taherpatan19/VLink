def printArray(string, n):
    for i in range(n):
        print (string[i],end=" ")

def sort(s,n):
    for i in range(1,n):
        temp=s[i]
        j=i-1
        while j>=0 and len(temp)<len(s[j]):
            s[j+1]=s[j]
            j-=1
        s[j+1]=temp
if __name__== "__main__":
    arr=["Taher", "am", "I", "Patanwala"]
    n=len(arr)
    sort(arr,n)
    printArray(arr,n)