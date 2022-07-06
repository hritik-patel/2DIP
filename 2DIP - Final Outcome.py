#A game application that compares two search term average monthly searches. The user has to guess which term has a higher or lower monthly search
#Import all useful libraries
import tkinter as tk
from data import data
import random

root = tk.Tk()
#Centre the window
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
positionRightLarge = int(root.winfo_screenwidth()/2 - windowWidth/2 - 100)
positionDownLarge = int(root.winfo_screenheight()/2 - windowHeight/2 - 50)

#Loading Screen
root.title('Loading!')
canvas_1 = tk.Canvas(root)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.resizable(False, False)
label = tk.Label(root, text="\n\n\n      Welcome, loading the      \n      Higher or Lower game!      \n\n\n")
label.config(font=('helvetica', 14))
label.pack()


#Time To Destroy
root.after(3000)
root.destroy()

#Creating the basic layout
root = tk.Tk()
root.title('Game')
canvas_1 = tk.Canvas(root, width = 400, height = 300) 
root.geometry("+{}+{}".format(positionRightLarge, positionDownLarge))
root.resizable(False,False) 
canvas_1.pack()
label = tk.Label(root, text='Higher or Lower!')
label.config(font=('helvetica', 14))
canvas_1.create_window(200, 25, window=label)

#Eligibility Process

#Name input
label_1 = tk.Label(root, text='Enter your Name:')
label_1.config(font=('helvetica', 10))
canvas_1.create_window(200, 70, window=label_1)
name_entry = tk.Entry (root) 
canvas_1.create_window(200, 110, window=name_entry)

#Age input
label_2 = tk.Label(root, text='Enter your Age:')
label_2.config(font=('helvetica', 10))
canvas_1.create_window(200, 140, window=label_2)
age_entry = tk.Entry (root) 
canvas_1.create_window(200, 180, window=age_entry)   

#Display exit button
exit_button = tk.Button(root, text='Exit', command=root.destroy)
exit_button.config(font=('helvetica', 10))
canvas_1.create_window(200, 255, window=exit_button)

#Create a 'clear' canvas function (Destory and replace)
def clear_draw():

    #Delete the canvas
    canvas_1.delete("all")
    label_1 = tk.Label(root, text='Higher or Lower!')
    label_1.config(font=('helvetica', 14))

    #Create a blank canvas
    canvas_1.create_window(200, 25, window=label_1)

#Add a score variable with a preset value of 0
score = 0

#Function to add one to the score
def addScore():
    global score
    score = score + 1

#Function to reset the score if the user decides to replay
def resetScore():
    global score

    #Using (score - score) as they will cancel each other out and equal to 0
    score = score - score

#Start the game
def main():

    #Clear the screen
    clear_draw()

    #Pick 2 random search terms
    first_term = random.choice(data)
    second_term = random.choice(data)

    #Ensure that the search terms are not the same
    while first_term == second_term:
        second_term = random.choice(data)

    #Question
    subtitle = tk.Label(root, text='Which term has the higher average monthly search?')
    #Helvecta and italic are the font
    subtitle.config(font=('helvetica', 10)  + ('italic',))
    canvas_1.create_window(200, 50, window=subtitle)

    #Create the first term label
    first_term_label = tk.Label(root, text=first_term['name'])
    first_term_label.config(font=('helvetica', 18))
    canvas_1.create_window(200, 100, window=first_term_label)

    label_or = tk.Label(root, text='or')
    label_or.config(font=('helvetica', 14))
    canvas_1.create_window(200, 140, window=label_or)

    #Create the second term label
    second_term_label = tk.Label(root, text=second_term['name'])
    second_term_label.config(font=('helvetica', 18))
    canvas_1.create_window(200, 180, window=second_term_label)

    #First option (Top option)
    def a():

        #If the user is correct play this if statement
        if first_term['search_count'] >= second_term['search_count']:
            clear_draw()

            #Say correct
            correct = tk.Label(root, text='Correct!')
            correct.config(font=('helvetica', 14))
            canvas_1.create_window(200, 100, window=correct)

            #As it is correct, add one to the score
            addScore()
            
            #Continue to next random question
            next_q = tk.Button(root, text='Next Question', command=main)
            next_q.config(font=('helvetica', 14))
            canvas_1.create_window(200, 180, window=next_q)

        #If the user is wrong, play this if statement
        elif first_term['search_count'] < second_term['search_count']:
            clear_draw()

            #Say wrong
            wrong = tk.Label(root, text='Wrong!')
            wrong.config(font=('helvetica', 14))
            canvas_1.create_window(200, 100, window=wrong)
            
            #Print answer and number of searchs
            ans = tk.Label(root, text=f'The correct answer was {second_term["name"]}, a {second_term["description"]} from {second_term["country"]}, which had {int(second_term["search_count"])} searches!',
            #Wraplength to make sure it fits inside the box
            wraplength=300, justify="center")
            ans.config(font=('helvetica', 10))
            canvas_1.create_window(200, 230, window=ans)

            #Print the final score of that game
            final_score = tk.Label(root, text='Your final score is: {}'.format(score))
            final_score.config(font=('helvetica', 14))
            canvas_1.create_window(200, 140, window=final_score)

            #Reset score in case the user decides to replay
            resetScore()

            #Display exit button
            exit_button = tk.Button(root, text='Exit', command=root.destroy)
            exit_button.config(font=('helvetica', 14))
            canvas_1.create_window(250, 180, window=exit_button)

            #Display replay button
            replay_button = tk.Button(root, text='Replay', command=main)
            replay_button.config(font=('helvetica', 14))
            canvas_1.create_window(150, 180, window=replay_button)

    #Second option (Bottom option)
    def b():

        #If the user is correct, play this if statement
        if first_term['search_count'] <= second_term['search_count']:
            clear_draw()

            #Say correct
            correct = tk.Label(root, text='Correct!')
            correct.config(font=('helvetica', 14))
            canvas_1.create_window(200, 100, window=correct)

            #As it is correct, add one to the score
            addScore()

            #Button to go to next round
            next_q = tk.Button(root, text='Next Question', command=main)
            next_q.config(font=('helvetica', 14))
            canvas_1.create_window(200, 180, window=next_q)
        
        #If the user is wrong, play this if statement
        elif first_term['search_count'] > second_term['search_count']:
            clear_draw()

            #Say wrong
            wrong = tk.Label(root, text='Wrong!')
            wrong.config(font=('helvetica', 14))
            canvas_1.create_window(200, 100, window=wrong)

            #Print answer and number of searchs
            ans = tk.Label(root, text=f'The correct answer was {first_term["name"]}, a {first_term["description"]} from {first_term["country"]}, which had {int(first_term["search_count"])} searches!',
            #Wraplength to make sure it fits inside the box
            wraplength=300, justify="center")
            ans.config(font=('helvetica', 10))
            canvas_1.create_window(200, 230, window=ans)
            
            #Print the final score of that game
            final_score = tk.Label(root, text='Your final score is: {}'.format(score))
            final_score.config(font=('helvetica', 14))
            canvas_1.create_window(200, 140, window=final_score)

            #Reset score in case the user decides to replay
            resetScore()

            #Display exit button
            exit_button = tk.Button(root, text='Exit', command=root.destroy)
            exit_button.config(font=('helvetica', 14))
            canvas_1.create_window(250, 180, window=exit_button)

            #Display replay button
            replay_button = tk.Button(root, text='Replay', command=main)
            replay_button.config(font=('helvetica', 14))
            canvas_1.create_window(150, 180, window=replay_button)




    #Create buttons for the two terms
    first_term_button = tk.Button(root, text=first_term['name'], command=a)
    canvas_1.create_window(200, 220, window=first_term_button)

    second_term_button = tk.Button(root, text=second_term['name'], command=b)
    canvas_1.create_window(200, 250, window=second_term_button)

    #Create the quit button
    quit_button = tk.Button(root, text='Quit', command=root.destroy)
    canvas_1.create_window(100, 280, window=quit_button)

#Check age and name
def checkage():

    #If name is not entered, display error
    if name_entry.get() == '':
        label_1 = tk.Label(root, text='          Please enter a valid name!           ')
        label_1.config(font=('helvetica', 6))
        canvas_1.create_window(200, 83, window=label_1)
        root.after(4000, label_1.destroy)
    
    #If name is not alphabetic, display error
    if name_entry.get() == (x.isalpha() for x in name_entry.get()):
        label_2 = tk.Label(root, text='          Please enter a valid name!           ')
        label_2.config(font=('helvetica', 6))
        canvas_1.create_window(200, 83, window=label_2)
        root.after(4000, label_2.destroy)

    #If age is a alphabet, or has a space in it display error
    if age_entry.get() != (x.isalpha() or x.isspace() for x in age_entry.get()):
        label_3 = tk.Label(root, text='          Please enter a valid age!        ')
        label_3.config(font=('helvetica', 6))
        canvas_1.create_window(200, 153, window=label_3)
        root.after(4000, label_3.destroy)

    #If age is not entered, display error
    if age_entry.get() == '':
        label_4 = tk.Label(root, text='          Please enter a valid age!        ')
        label_4.config(font=('helvetica', 6))
        canvas_1.create_window(200, 153, window=label_4)
        root.after(4000, label_4.destroy)

    #If under 8 years old, display error message
    if  int(float(age_entry.get())) <= 8:
        label_5 = tk.Label(root, text='You are too young to play this game!')
        label_5.config(font=('helvetica', 10))
        canvas_1.create_window(200, 210, window=label_5)
        root.after(4000, label_5.destroy)

    #If everything is correct start the game
    else:
        main()
    
#Button to check if age and name are correct
checkage = tk.Button(text='Start the game!', command=checkage, bg='brown', fg='black', font=('helvetica', 10))
canvas_1.create_window(200, 230, window=checkage)

#End of program
root.mainloop()