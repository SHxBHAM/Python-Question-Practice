n=int(input("please enter your number :"))
if n % 2 != 0 :
    print("Weird")
elif n%2==0 and 2<=n>=5 :
    print("Not Weird")
elif n%2 == 0 and 20>=n>=6 :
    print ("Weird")
elif n%2==0 and n>20 :
    print ("Not Weird")       
       