import numpy as np
print('Welcome to rack-paper-scissors')
print('Here are the rules')
print('Rock beats scissors')
print('Scissors beat paper')
print('Paper beats rock')
d=['Rock','Paper','Scissors']
while True:
    while True:
        choice=input('Enter your choice:')
        ok=1 if choice in d else 0
        if ok:
            print('OK')
            break
        else:
            print('Please choose on of the three options')
    PCchoice=np.random.randint(0,3)
    if d.index(choice)==PCchoice:
        print(d[PCchoice],' vs ',choice)
        print ('ITS A DRAW!')
    elif d.index(choice)==PCchoice+1:
        print(d[PCchoice],' vs ',choice)
        print ('YOU WON!')
    elif PCchoice==d.index(choice)+2:
        print(d[PCchoice],' vs ',choice)
        print ('YOU WON!')
    elif PCchoice==d.index(choice)+1:
        print(d[PCchoice],' vs ',choice)
        print ('YOU LOST!')
    elif d.index(choice)==PCchoice+2:
        print(d[PCchoice],' vs ',choice)
        print ('YOU LOST!')
    print('Do you want to play one more round?? Y/N')
    while True:
        ans=input(' ')
        if ans not in ['Y','N','y','n','yes','no']:
            print('Choose Y/N please')
        else:
            if ans in('Y','y','yes'):
                break
            elif ans in('N','n','no'):
                print('Thanks for playing!')
                exit()


        