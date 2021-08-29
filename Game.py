import random
number=random.randint(1,9)
chances=0

print('Guess A Number between 1 to 9')

while chances < 5:
     guess=int(input('Enter Your Number:'))
  
     if guess==number:
         print('Wohoo! You guessed it right')
     else: 
        print('Wrong!')
     chances+=1
if not chances <5:
    print('You loose!')     

