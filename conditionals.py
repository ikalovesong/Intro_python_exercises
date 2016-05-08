

my_name="aika"
name=raw_input("whta is your name?")

if str(name)<my_name:
	print "my name is greater"
elif str(name)>my_name:
	print "his name is greater"
else:
	print "Our name are equal"


date=raw_input("What is the date?")

if int(date)<15:
	print 'The month is still young'
else:
	print "Oh whe are half way there"

	

today=raw_input("what week day it is?")

if str(today)=="Monday":
	print "Yay class day"
elif str(today)=="Tuesday":
	print "Sigh, it's only Tuesday"
elif str(today)=="Wedneasday":
	print "Humpday"
elif str(today)=="Thursday":
	print "#tbt"
elif str(today)=="Friday":
	print "TGIF!"
else:
	print "yeah, it's the weekend"



age=raw_input("what is your age?")

if int(age)>=18 and int(age)>=21:
	print "Yeah, I can vote and drink"
elif int(age)>=18 and int(age)<=21:
	print "I can vote but I cannot drink"
else:
	print "Aww, I cannot vote and go to bar"



if 8%2==0 and 9%2==0:  
	print "both numbers are even"
elif 9%2==0 and 9%2==0:
	print "8 is even and 9 is odd"
elif 8%2!=0 and 9%2==0:
	print "8 is odd and 9 is even."
else:
	print "both numbers are odd"
	

color=raw_input("what is your fav color? ")

if color=="red" or color=="red" or color=="blue":
	print  "My favorite color is primary!"
else:
	print "My favorite color is secondary! "






































