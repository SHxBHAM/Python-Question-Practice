#take 5 name inputs and take age inputs print the oldest persons name
name1=str(input("please enter your name:"))
name2=str(input("please enter your name:"))
name3=str(input("please enter your name:"))
name4=str(input("please enter your name:"))
name5=str(input("please enter your name:"))

age1 = int(input( "please enter your age:"))
age2 = int(input( "please enter your age:"))
age3 = int(input( "please enter your age:"))
age4 = int(input( "please enter your age:"))
age5 = int(input( "please enter your age:"))

if age1>age2 and age1>age3 and age1>age4 and age1>age5:
    print (name1,"is the oldest")
elif age2>age1 and age2>age3 and age2>age4 and age2>age5:
    print (name2,"is the oldest")
elif age3>age1 and age3>age2 and age3>age4 and age3>age5:
    print (name3,"is the oldest")
elif age4>age1 and age4>age3 and age4>age2 and age4>age5:
    print (name4,"is the oldest")    
elif age5>age1 and age5>age3 and age5>age4 and age5>age2:
    print (name5,"is the oldest")
else:
    print(name1,name2,name3,name4,name5,"are of same age")
    

