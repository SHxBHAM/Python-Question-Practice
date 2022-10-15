num = int(input("please enter your number:"))
last_digit=num%10

if last_digit % 3==0:
    print ("the last digit of the number is divisible by 3 :)")
elif last_digit%3!=0:
    print("the last digit of the number is not divisible by 3 :(")    
else :
    print ("invalid data")