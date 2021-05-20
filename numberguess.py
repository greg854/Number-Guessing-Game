import PySimpleGUI as sg
import random as rand

LOW_VALUE = 50
HIGH_VALUE = 500

def checkUserInput(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
            return False
        except ValueError:
            print("No.. input is not a number. It's a string")
            return False

def findDifference(userGuess, pickedNumber):
    difference = userGuess - pickedNumber
    return difference


def compareNumber(userGuess, pickedNumber):
    difference = findDifference(userGuess, pickedNumber)

    if (difference == 0):
        sg.popup('You Guessed it!!!', text_color='blue', background_color='light slate gray')
    elif (difference <= -1):
        sg.popup('Too Low!!', text_color='green')
    else:
        sg.popup('Too High!!', text_color='orchid')


def setup():
    sg.theme('DarkTeal2')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('I\'m thinking of a number between {} and {}'.format(LOW_VALUE,HIGH_VALUE))],
              [sg.Text('Enter your guess'), sg.InputText()],
              [sg.Button('Submit'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Try To Guess My Number!', layout)

    # Create the number
    randomNumber = rand.randint(LOW_VALUE, HIGH_VALUE)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        if event == 'Submit':
            isInt = checkUserInput(values[0])
            if(isInt == True):
                compareNumber(int(values[0]), randomNumber)
            else:
                sg.popup('Enter an integer, fool!!!',text_color='magenta', background_color='coral')
            print(randomNumber)

    window.close()


# Press the green button in the gutter to run the script.
if _name_ == '_main_':
    setup()
