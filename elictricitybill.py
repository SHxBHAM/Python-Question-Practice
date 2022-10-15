units=int(input("please enter the meter reading (units used):"))

if units >= 0 and  units <= 100 :
    print ("your elictricity bill is :00")
elif units>100 and units<200:
    print ("your elictricity bill is :", units*5,"Rs") 
elif units>= 200 and units<10000000 :
    print ("your electricity bill is :",units*10,"Rs")
else :
    print ("data invalid")           