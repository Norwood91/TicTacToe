from tkinter import *
from tkinter import messagebox
import time

screen = Tk()
screen.title('Tic-Tac-Toe')


# X = True, O = False
clicked = True
# Keeps track of the count of moves in the game, so we can declare a tie if need be
count = 0

def disable_all_buttons():
    button_one.config(state=DISABLED)
    button_two.config(state=DISABLED)
    button_three.config(state=DISABLED)
    button_four.config(state=DISABLED)
    button_five.config(state=DISABLED)
    button_six.config(state=DISABLED)
    button_seven.config(state=DISABLED)
    button_eight.config(state=DISABLED)
    button_nine.config(state=DISABLED)

# Check to see if someone won
def check_if_won():
    global winner
    winner = False

    if button_one['text'] == 'X' and button_two['text'] == 'X' and button_three['text'] == 'X':
        button_one.config(bg='#54BAB9')
        button_two.config(bg='#54BAB9')
        button_three.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_four['text'] == 'X' and button_five['text'] == 'X' and button_six['text'] == 'X':
        button_four.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_six.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_seven['text'] == 'X' and button_eight['text'] == 'X' and button_nine['text'] == 'X':
        button_seven.config(bg='#54BAB9')
        button_eight.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_one['text'] == 'X' and button_four['text'] == 'X' and button_seven['text'] == 'X':
        button_one.config(bg='#54BAB9')
        button_four.config(bg='#54BAB9')
        button_seven.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_two['text'] == 'X' and button_five['text'] == 'X' and button_eight['text'] == 'X':
        button_two.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_eight.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_three['text'] == 'X' and button_six['text'] == 'X' and button_nine['text'] == 'X':
        button_three.config(bg='#54BAB9')
        button_six.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_one['text'] == 'X' and button_five['text'] == 'X' and button_nine['text'] == 'X':
        button_one.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    elif button_three['text'] == 'X' and button_five['text'] == 'X' and button_seven['text'] == 'X':
        button_three.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_seven.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'X wins the game!')
        disable_all_buttons()

    # Start of O
    elif button_four['text'] == 'O' and button_five['text'] == 'O' and button_six['text'] == 'O':
        button_four.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_six.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', ' wins the game!')
        disable_all_buttons()

    elif button_seven['text'] == 'O' and button_eight['text'] == 'O' and button_nine['text'] == 'O':
        button_seven.config(bg='#54BAB9')
        button_eight.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()

    elif button_one['text'] == 'O' and button_four['text'] == 'O' and button_seven['text'] == 'O':
        button_one.config(bg='#54BAB9')
        button_four.config(bg='#54BAB9')
        button_seven.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()

    elif button_two['text'] == 'O' and button_five['text'] == 'O' and button_eight['text'] == 'O':
        button_two.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_eight.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()

    elif button_three['text'] == 'O' and button_six['text'] == 'O' and button_nine['text'] == 'O':
        button_three.config(bg='#54BAB9')
        button_six.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()

    elif button_one['text'] == 'O' and button_five['text'] == 'O' and button_nine['text'] == 'O':
        button_one.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_nine.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()

    elif button_three['text'] == 'O' and button_five['text'] == 'O' and button_seven['text'] == 'O':
        button_three.config(bg='#54BAB9')
        button_five.config(bg='#54BAB9')
        button_seven.config(bg='#54BAB9')
        winner = True
        messagebox.showinfo('Congrats!', 'O wins the game!')
        disable_all_buttons()
    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo('Tie', 'Game ended in a TIE. Reset game to play again!')
        disable_all_buttons()

def button_clicked(button):
    global clicked, count
    if button['text'] == ' ' and clicked == True:
        button['text'] = 'X'
        clicked = False
        count += 1
        check_if_won()
    elif button['text'] == ' ' and clicked == False:
        button['text'] = 'O'
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror('Error', 'There\'s already an X or O in this box. Please choose another!')

# Start game over
def reset_game():
    global button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight, button_nine
    global clicked, count
    clicked = True
    count = 0
    # Build our buttons
    button_one = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                        height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_one))
    button_two = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                        height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_two))
    button_three = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                          height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_three))

    button_four = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                         height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_four))
    button_five = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                         height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_five))
    button_six = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                        height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_six))

    button_seven = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                          height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_seven))
    button_eight = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                          height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_eight))
    button_nine = Button(screen, text=' ', font=('Helvetica', 25, 'bold'),
                         height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(button_nine))

    # Grid buttons to the screen

    button_one.grid(row=0, column=0)
    button_two.grid(row=0, column=1)
    button_three.grid(row=0, column=2)

    button_four.grid(row=1, column=0)
    button_five.grid(row=1, column=1)
    button_six.grid(row=1, column=2)

    button_seven.grid(row=2, column=0)
    button_eight.grid(row=2, column=1)
    button_nine.grid(row=2, column=2)



# Create menu
my_menu = Menu(screen)
screen.config(menu=my_menu)

menu_options = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=menu_options)
menu_options.add_command(label='Reset Game', command=reset_game)
reset_game()
screen.mainloop()
