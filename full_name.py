name= input (" Please enter your full name-")
surname= input ("Please enter your surname-")
fullname= name + " " + surname
if len(name)==0:
    print ('"You haven\'t entered anything in name. Please enter your name."')
elif len (surname)==0:
    print ('"You haven\'t entered anything in surname. Please enter your surname."')
elif len (name and surname) <4:
    print ('"you have entered less than 4 characters. Please make sure you enter full name."')
elif len (name + surname) >25:
    print ('"you have entered more than 25 characters. Please make sure you have only entered your full name."')
else:
    print('"Thank you for entering your name."')
    print (fullname)


""" 1) reference used if_example.py and pdf DS T03 beginners control structure. task 3 video of logical operators used as a reference 
2) Used (\)escape character in the string to include (') and make sure (') dont end the atring
3) Also used concatenation to reflect full name. Defined name and surname seperately to make sure user input both names to avoid any confusion.
4) line 4 and 6 name and surname both are checked seperately if user is not living it blank.
5) used (and) as a logical conjunction operator
6) line 8 checks both name and surname if contains less < 4 characters or not
7) line 10 checks if both name and surname jointly is no more than 25 characters"""