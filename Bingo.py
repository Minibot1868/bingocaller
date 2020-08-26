#Importing functions
import random
import time
import webbrowser
import os



#Welcome Message
print('Welcome to Bingo Caller')

print('Would you like to send the developers an email about this program?')
questionEmail = input('Enter \'Y\' for yes and \'N\' for no: ')
if questionEmail == 'y':
       webbrowser.open('mailto:software.bingocallerapp@outlook.com', new=2)
else:
       print('Would you like to check for updates?')
       updater = input('Enter \'Y\' for yes and \'N\' for no: ')
       if updater == 'y':
              os.startfile("C:\\Program Files (x86)\\Bingo Caller\\Updater.exe")  
       
       else:
              print('After you type a value, press ENTER to submit it.')
              #Pause
              time.sleep(0.4)

              #Main process
              def begin():
                     try: no_of_rounds = int(input('How many numbers would you like generated for this: '))
                     except ValueError:
                            no_of_rounds = int(input('Please enter a valid number '))
              #Checks if the user is happy with the amount of numbers being called in the game
                     confirm_rounds = input('Are you sure? Enter \'Y\' for yes and \'N\' for no: ')
                     #Loops until valid input
                     while confirm_rounds != 'y' and confirm_rounds != 'n':
                            
                            confirm_rounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

                     #Loops until user sure about number of rounds
                     while confirm_rounds == 'n':
                            try: no_of_rounds = int(input('How many numbers would you like generated for this game? '))
                            except ValueError:
                                   no_of_rounds = int(input('Please enter a valid number '))
                            confirm_rounds = input('Are you sure? Enter \'Y\' for yes and \'N\' for no: ')
                     while confirm_rounds != 'y' and confirm_rounds != 'n':
                            confirm_rounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

                     #If happy, the loops end, and the code contines
                     if confirm_rounds == 'y':
                            print('Lets play bingo!')
                            ready = input('Press ENTER to get your first number: ')
                     #To start the game, the user can hit ENTER. Any other value is also accepted to avoid errors.
                     if ready >= '':
                     #The game has started, and a variable is declared as a random number between 0 and 90
                                   next_num = random.randint(0,90)
                     #A list is created for numbers already called to go in
                                   already_called = []
                     #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                                   x = 0
                     while x < no_of_rounds:
                     #The number is reset if it has already been called; x stays the same
                            if next_num in already_called:
                                          next_num = random.randint(1,90)
                                          
                     #If the number hasn't been called, then it is included in the list, printed, and reset.
                            elif next_num not in already_called:
                                   already_called.append(next_num)
                                   print (next_num)
                                   next_num = random.randint(1,90)
                                   input("Press Enter to view next drawn number")
                                   x +=1
                     #Ends the loop when conditions met
                            else:
                                   break
                     
                     #When all numbers are called...
                     print ('You have reached your selected amount of numbers')
                     time.sleep(0.5)
                     print('Thank you for playing Bingo Caller')

              #Actually runs the game
              begin()
              #Asks if they want to play again
              again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
              #Loops until valid input
              while again != 'y' and again != 'x':
                     again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')
              #The game loops until the user declars 'x'
              while again == 'y':
                     begin()
                     again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
              while again != 'y' and again != 'x':
                     again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')

              if again == 'x':
                     print ('Goodbye!')
                     time.sleep(1)