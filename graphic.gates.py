
# graphic.gates.py

from graphics import *

# Function to draw an AND gates
def draw_and(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y-size/4
    # Outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y2)).draw(win)
    Line(Point(x1,y2),Point(x2,y1)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)
        
# Function to draw an OR gate
def draw_or(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_not(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2

    Line(Point(x1,y1), Point(x1,y2)).draw(win)
    Line(Point(x2,y1), Point(x1,y2)).draw(win)
    Line(Point(x1,y1), Point(x2,y)).draw(win)

    Line(Point(x2+8,y),Point(x2+18,y)).draw(win)
    Line(Point(x1,y),Point(x1-10,y)).draw(win)
    Circle(Point(x2+3,y),5).draw(win)
    
def draw_xor(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4

    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)

    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)
    Arc(Point(x1-size/2-8,y1+5),Point(x1+size/2-8,y2-5)).draw(win)

def draw_nand(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4

    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)

    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size+8,y),Point(x+size+18,y)).draw(win)
    Circle(Point(x+4+size,y),5).draw(win)

def box(x, y, text, win):
    x1, x2 = x+30,x-30
    y1, y2 = y+20,y-30
    Rectangle(Point(x1,y1),Point(x2,y2)).draw(win)
    t = Text(Point(x,y),text).draw(win)

def and_button(win):
    click = win.getMouse()
    y = click.getY()
    x = click.getX()
    if 20<x<80 and 30<y<70:
        newClick = win.getMouse()
        x1 = newClick.getX()
        y1 = newClick.getY()
        draw_and(x1, y1, 60, win)

def or_button(win):
    click = win.getMouse()
    y = click.getY()
    x = click.getX()
    if 20<x<80 and 130<y<170:
        newClick = win.getMouse()
        x1 = newClick.getX()
        y1 = newClick.getY()
        draw_or(x1, y1, 60, win)

def not_button(win):
    click = win.getMouse()
    y = click.getY()
    x = click.getX()
    if 20<x<80 and 230<y<270:
        newClick = win.getMouse()
        x1 = newClick.getX()
        y1 = newClick.getY()
        draw_not(x1, y1, 60, win)

def xor_button(win):
    click = win.getMouse()
    click = win.getY()
    x = click.getX()
    if 20<x<80 and 330<y<370:
        newClick = win.getMouse()
        x1 = newClick.getX()
        y1 = newClick.getY()
        draw_not(x1, y1, 60, win)

def nand_button(win):
    click = win.getMouse()
    y = click.getY()
    x = click.getX()
    if 20<x<80 and 430<y<470:
        newClick = win.getMouse()
        x1 = newClick.getX()
        y1 = newClick.getY()
        draw_nand(x1, y1, 60, win)

def buttons(win):
    box(50,50,"AND",win)
    box(50,150,"OR",win)
    box(50,250,"NOT",win)
    box(50,350,"XOR",win)
    box(50,450,"NAND",win)
    while True:
        and_button(win)
        or_button(win)
        not_button(win)
        xor_button(win)
        nand_button(win)

def main():
    win = GraphWin("Title", 600, 600)
    buttons(win)

main()
     
    
