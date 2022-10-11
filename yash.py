age1 = int(input("please enter age :"))
age2 = int(input("please enter age :"))
age3 = int(input("please enter age :"))

if age1>age2 and age1>age3:
    print ("age 1 is the greatest")
elif age2>age1 and age2>age3: 
     print ("age 2 is the greatest")
elif age3>age1 and age3>age2:   
     print("age 3 is the greatest")  
else:
    print ("all ages are equal")      
