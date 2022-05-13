"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from emoji import emojize

from freegames import path

car = path('car.gif')
emojis=[u'\U0001F347', u'\U0001F348', u'\U0001F349', u'\U0001F34A', u'\U0001F34B', u'\U0001F34C', u'\U0001F34D', u'\U0001F34E', u'\U0001F34F', u'\U0001F350', u'\U0001F351', u'\U0001F352', u'\U0001F353', u'\U0001F95D', u'\U0001F345', u'\U0001F965',u'\U0001F347', u'\U0001F348', u'\U0001F349', u'\U0001F34A', u'\U0001F34B', u'\U0001F34C', u'\U0001F34D', u'\U0001F34E', u'\U0001F34F', u'\U0001F350', u'\U0001F351', u'\U0001F352', u'\U0001F353', u'\U0001F95D', u'\U0001F345', u'\U0001F965']
tiles = list(emojis) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

tapCount=0
founds = 0 
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tapCount
    global founds 
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
    tapCount +=1

    founds=0
    for a in hide:
        if a == False:
          founds += 1

   

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    if founds==4:
        up()
        goto(0, 0)
        color('green')
        write('YOU WIN!!', font=('Arial', 30, 'normal'), align='center')

    goto(-240,150)#-240,150
    color('green')
    write(tapCount, font=('Arial', 30, 'normal'), align='center')
    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(540, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
