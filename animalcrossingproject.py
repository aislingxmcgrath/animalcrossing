import pyinputplus
import pyinputplus as pyip

print('Welcome to the Animal Crossing Personality Evaluator!')

while True:
     prompt = 'Would you like to play? yes or no '
     answer = pyip.inputYesNo(prompt)
     if answer == 'yes':
         print('Great! First question: ')
         print('Are you male or female?')
         gender = input()
         if gender == 'male':
             print('Cool! You said male. Next question: ')
             print('What is your favorite pasttime?')
             print('A) Gossiping')
             print('B) Exercising')
             print('C) Sleeping')
             print('D) Shopping')
             q2 = input()
             if q2 == 'A':
                 print('You are Cranky! ')
             elif q2 == 'B':
                 print('You are a Jock! ')
             elif q2 == 'C':
                 print('You are Lazy! ')
             elif q2 == 'D':
                 print('You are Smug!')
             break

         elif gender == 'female':
             print('Cool! You said female. Next question: ')
             print('How would your friends describe you?')
             print('A) Pleasant')
             print('B) Bubbly')
             print('C) Uptight')
             print('D) Sassy')
             q2f = input()
             if q2f == 'A':
                 print('You are Normal! ')
             elif q2f == 'B':
                 print('You are Peppy! ')
             elif q2f == 'C':
                 print('You are Snooty! ')
             elif q2f == 'D':
                 print('You are Uchi!')
             break
     elif answer == 'no' :
        print('Okay! Maybe next time.')
        break
     else:
          print('Please enter yes or no.')
          continue

print('Thanks For playing!')
