#A game application that compares two search term average monthly searches. The user has to guess which term has a higher or lower monthly search
#Import all useful libraries
import tkinter as tk
from data import data
import random

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#Eligibility Process

label1 = tk.Label(root, text='Higher or Lower!')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your Name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 80, window=label2)

name_entry = tk.Entry (root) 
canvas1.create_window(200, 110, window=name_entry)

label2 = tk.Label(root, text='Enter your Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 140, window=label2)

age_entry = tk.Entry (root) 
canvas1.create_window(200, 180, window=age_entry)

#Clear window function

def clear_draw():
    canvas1.delete("all")
    label1 = tk.Label(root, text='Higher or Lower!')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

#Game

def main():
    #Start the quiz
    #Clear the screen
    clear_draw()
    first_term = random.choice(data)
    second_term = random.choice(data)
    while first_term == second_term:
        second_term = random.choice(data)

    subtitle = tk.Label(root, text='Who has the higher average monthly search?')
    #Helvecta and italic are the font
    subtitle.config(font=('helvetica', 10)  + ('italic',))
    canvas1.create_window(200, 50, window=subtitle)

    #Create the first term label
    first_term_label = tk.Label(root, text=first_term['name'])
    first_term_label.config(font=('helvetica', 18))
    canvas1.create_window(200, 100, window=first_term_label)

    label_or = tk.Label(root, text='or')
    label_or.config(font=('helvetica', 14))
    canvas1.create_window(200, 140, window=label_or)

    #Create the second term label
    second_term_label = tk.Label(root, text=second_term['name'])
    second_term_label.config(font=('helvetica', 18))
    canvas1.create_window(200, 180, window=second_term_label)
    def a():
        if first_term['search_count'] > second_term['search_count']:
            clear_draw()

            #Say correct!
            correct = tk.Label(root, text='Correct!')
            correct.config(font=('helvetica', 14))
            canvas1.create_window(200, 100, window=correct)

            next_q = tk.Button(root, text='Next Question', command=main)
            next_q.config(font=('helvetica', 14))
            canvas1.create_window(200, 180, window=next_q)

        elif first_term['search_count'] < second_term['search_count']:
            clear_draw()

            #Say wrong!
            wrong = tk.Label(root, text='Wrong!')
            wrong.config(font=('helvetica', 14))
            canvas1.create_window(200, 100, window=wrong)

            ans = tk.Label(root, text=f'The correct answer is {first_term["name"]} \n they had {int(first_term["search_count"])} Searches!')
            ans.config(font=('helvetica', 14))
            canvas1.create_window(200, 140, window=ans)

            #Show exit button
            exit_button = tk.Button(root, text='Exit', command=root.destroy)
            exit_button.config(font=('helvetica', 14))
            canvas1.create_window(200, 180, window=exit_button)


    def b():
        if first_term['search_count'] < second_term['search_count']:
            clear_draw()

            #Say correct!
            correct = tk.Label(root, text='Correct!')
            correct.config(font=('helvetica', 14))
            canvas1.create_window(200, 100, window=correct)

            next_q = tk.Button(root, text='Next Question', command=main)
            next_q.config(font=('helvetica', 14))
            canvas1.create_window(200, 180, window=next_q)
        

        elif first_term['search_count'] > second_term['search_count']:
            clear_draw()

            #Say wrong!
            wrong = tk.Label(root, text='Wrong!')
            wrong.config(font=('helvetica', 14))
            canvas1.create_window(200, 100, window=wrong)

            ans = tk.Label(root, text=f'The correct answer is {second_term["name"]} \n they had {int(second_term["search_count"])} Searches!')
            ans.config(font=('helvetica', 14))
            canvas1.create_window(200, 140, window=ans)

            exit_button = tk.Button(root, text='Exit', command=root.destroy)
            exit_button.config(font=('helvetica', 14))
            canvas1.create_window(200, 180, window=exit_button)

    #Create buttons for the two terms
    first_term_button = tk.Button(root, text=first_term['name'], command=a)
    canvas1.create_window(200, 220, window=first_term_button)

    second_term_button = tk.Button(root, text=second_term['name'], command=b)
    canvas1.create_window(200, 250, window=second_term_button)

    #Create the quit button
    quit_button = tk.Button(root, text='Quit', command=root.destroy)
    canvas1.create_window(100, 280, window=quit_button)


#Check user details

def checkage():
    if int(age_entry.get()) < 8:
        label3 = tk.Label(root, text='You are too young to play this game!')
        label3.config(font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)
    elif age_entry.get() == '':
        label3 = tk.Label(root, text='         Please enter your age!            ' )
        label3.config(font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)
    elif name_entry.get() == '':
        label3 = tk.Label(root, text='          Please enter your name!           ')
        label3.config(font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)
    else:
        main()
    


    
checkage = tk.Button(text='Start The Quiz!', command=checkage, bg='brown', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 230, window=checkage)

root.mainloop()