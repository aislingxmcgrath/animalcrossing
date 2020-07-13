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
             q2 = q2.upper()
             if q2 in ('A','B','C','D'):
                  if q2 == 'A':
                      print('You are Cranky! ')
                      break
                  elif q2 == 'B':
                      print('You are a Jock! ')
                      break
                  elif q2 == 'C':
                      print('You are Lazy! ')
                      break
                  elif q2 == 'D':
                      print('You are Smug!')
                      break
             else:
                       print('Please enter A,B,C or D.')
                       continue

         elif gender == 'female':
             print('Cool! You said female. Next question: ')
             print('How would your friends describe you?')
             print('A) Pleasant')
             print('B) Bubbly')
             print('C) Uptight')
             print('D) Sassy')
             q2f = input()
             q2f = q2f.upper()
             if q2f == 'A':
                 print('You are Normal! ')
                 break
             elif q2f == 'B':
                 print('You are Peppy! ')
             elif q2f == 'C':
                 print('You are Snooty! ')
                 break
             elif q2f == 'D':
                 print('You are Uchi!')
                 break
             else:
                 print('Please enter A,B,C or D')
                 continue
            
         else:
             print('Please enter male or female')
             continue
     elif answer == 'no' :
        print('Okay! Maybe next time.')
        break
     else:
          print('Please enter yes or no.')
          continue

print('Thanks For playing!')
