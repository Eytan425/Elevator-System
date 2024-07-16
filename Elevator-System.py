import tkinter as tk
import pyttsx3
import random

def text_to_speech(value):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)
    elevators = ['A', 'B', 'C', 'D']
    chosen_elevator = random.choice(elevators)
    elevator = elevator_floor(chosen_elevator,value)
    try:
        level = int(value)
        if -1 <= level <= 12:
            engine.say(f"Elevator {elevator} is the closest. He is at level {generate_floor()}")
            engine.say(f"Elevator {elevator} to level {level}")
        else:
            engine.say("The level input doesn't exist!")
    except ValueError:
        engine.say("Invalid input! Please enter a valid number.")
    
    engine.runAndWait()
    
    
    global clicked_values
    clicked_values = ""
    display_label.config(text=clicked_values)

def on_button_click(value):
    global clicked_values
    clicked_values += value
    display_label.config(text=clicked_values)
    root.after(260, speak_clicked_values)

def speak_clicked_values():
    global clicked_values
    if clicked_values:
        text_to_speech(clicked_values)
def generate_floor():
    num = random.randint(-1,13)
    
    return num
def elevator_floor(chosen_elevator, value):
    '''closest elevator'''
    a_floor = generate_floor()
    b_floor = generate_floor()
    c_floor = generate_floor()
    d_floor = generate_floor()
    floors = [a_floor, b_floor,c_floor,d_floor]
    elevator = ['A', 'B', 'C', 'D']
    index = 0
    closest = 12
    for i in range(len(floors)):
        if(int(value) - floors[i] < closest):
            closest = floors[i]
            index = i
    return elevator[index]      


# def clear_clicked_values():
#     global clicked_values
#     clicked_values = ""
#     display_label.config(text=clicked_values)

root = tk.Tk()
root.title("Numpad")

frame = tk.Frame(root)
frame.pack()

clicked_values = ""

display_label = tk.Label(frame, text="", width=20, height=2, relief="sunken", anchor="e")
display_label.grid(row=0, column=0, columnspan=3)

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '-', '0', '*'
]

row_val = 1
col_val = 0

for button in buttons:
    # if button == 'Clear':
    #     command = clear_clicked_values
    # else:
    #     command = lambda x=button: on_button_click(x)
    command = lambda x=button:on_button_click(x)
        
    tk.Button(frame, text=button, width=5, height=2, command=command).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# speak_button = tk.Button(root, text="Speak", command=speak_clicked_values)
# speak_button.pack(pady=5)

root.mainloop()