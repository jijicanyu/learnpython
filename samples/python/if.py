#!usr/bin/python
#filename:if.py

number=23
guess=int(raw_input('Enter an interger:'))

if guess==number:
    print 'Congratulations,you guessed it.'
    print '(but you do not win any prizes!)'
elif guess<number:
    print 'No,it is a little highter than that'
else:
    print 'No,it is a little lower than that'
print 'Done'
    
