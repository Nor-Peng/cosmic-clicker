from pygame_widgets.button import Button
from config import game_window
flag = False
e = 1
miss = 1
def _(x, y):
    global e
    global flag
    global miss
    e = x
    miss = y
    print(e)
    buttonez.hide()
    buttonnorm.hide()
    buttonhard.hide()
    flag = True
def callbutons():
    global buttonez
    global buttonnorm
    global buttonhard
    buttonez = Button(
        game_window,  
        100,  
        100,  
        300,  
        150,  

        
        text='EASY',  
        fontSize=50,
        margin=20,  
        inactiveColour=(0, 200, 0),  
        hoverColour=(0, 200, 150),  
        pressedColour=(150, 200, 0),  
        radius=20,  
        onClick=lambda: _(2, 6)
    )                       
    buttonnorm = Button(
        game_window,  
        450,  
        100,  
        300,  
        150,  

        
        text='NORMAL',  
        fontSize=50,
        margin=20,  
        inactiveColour=(255, 125, 0),  
        hoverColour=(255, 140, 0),  
        pressedColour=(255, 77, 183),  
        radius=20,  
        onClick=lambda: _(1, 4)
    )                     
    buttonhard = Button(
        game_window,  
        800,  
        100,  
        300,  
        150,  

        
        text='HARD',  
        fontSize=50,
        margin=20,  
        inactiveColour=(255, 0, 0),  
        hoverColour=(178, 34, 34),  
        pressedColour=(178, 34, 34),  
        radius=20,  
        onClick=lambda: _(0.5, 3)
    )