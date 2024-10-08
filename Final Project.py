from karel.stanfordkarel import *

def main():
    
    for i in range(4):
        painting_green()
        
    move()
    turn_left()
    move()   
    
    for i in range(4):
        painting_blue()
        
    moving()

    for i in range(4):
        painting_cyan()
    
    moving()
    
    for i in range(4):
        painting_pink()  

    moving()
    
    for i in range(4):
        painting_white() 



def painting_green():
    for i in range(9):
        paint_corner('GREEN')
        put_beeper()
        move()
    paint_corner('GREEN')
    turn_left()

def painting_blue():
    for i in range(7):
        paint_corner('BLUE')
        move()
    paint_corner('BLUE')
    turn_right()
    
def painting_cyan():
    for i in range(5):
        paint_corner('CYAN')
        put_beeper()
        move()
    paint_corner('CYAN')
    turn_right()
    
def painting_pink():
    for i in range(3):
        paint_corner('PINK')
        move()
    paint_corner('PINK')
    turn_right()
    
def painting_white():
    for i in range(1):
        paint_corner('GRAY')
        put_beeper()
        move()
    paint_corner('GRAY')
    turn_right()
    
def moving():
    turn_right()      
    move()
    turn_left()
    move()   

def turn_right():
    turn_left()
    turn_left()
    turn_left()
            
        

    
        
    


# don't change this code
if __name__ == '__main__':
    main()