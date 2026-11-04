def enter_arena () :
    print("Obo Jr. enters the Code Arena, ready for battle!")
 #calling the function
enter_arena()

def math_battle(number_1, number_2, Operator) :
    if Operator == '+':
        print(number_1 + number_2)
        
    elif Operator == '-':
        print(number_1 - number_2)
        
    elif Operator == '*':
        print(number_1 * number_2)
        
    elif Operator == '/':
        print(number_1 / number_2)
        
        
math_battle(5, 3, '*')

def element_blast(element):

    if element == 'fire':
        print("Obo Jr. blasts fire!")
        
    elif element == 'water':
        print("Obo Jr. blasts water")
        
    elif element == 'air':
        print("Obo Jr. blasts wind")
        
    elif element == 'earth':
        print("Obo Jr. blasts rocks")
        
element_blast('water')

def shape_solver(shape, dimension1, dimension2=0):

    if shape == 'circle':
        print (3.14 * dimension1)
    
    elif shape =='rectangle':
        print(dimension1 * dimension2)
        
    elif shape =='square':
        print(dimension1 * dimension2)
        
shape_solver('circle',7)

def final_battle(health, energy, wisdom):
    power = (health + energy) * wisdom / 2
    if power >120:
        print ('Obo Jr. defeats the Arena Boss!')
        
    else: print('Obo Jr.Loses to the arena boss')
    
final_battle(240,73,68)
