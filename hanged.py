import random

print("¡Ahorcado!")
print("------------------------------")

diccionarioPalabras = ["ReactJS", "MUI", "AngularJS", "TypeScript"]

randomPalabra = random.choice(diccionarioPalabras)

for i in randomPalabra:
    print("__", end =" ")

def imprimirLienas():
    print("\r")
    for char in randomPalabra:
        print("\u203E", end=" ")

longitud_palabra = len(randomPalabra)
veces_equibocada = 0
index_actual = 0
letras_correctas = []
letras_correctas_actuales = 0


while(longitud_palabra != 5 and letras_correctas_actuales != letras_correctas_actuales):
    print("\nLetras adivinadas: ")
    for letter in letras_correctas:
        print(letter, end =" ")
    

def imprimirPalabras(palabras):
    contador = 0
    correctas = 0

    for char in randomPalabra:
        if(char in palabras):
            print(randomPalabra[contador], end= " ");
            correctas+=1 
        else:
            print(" ", end=" ")
        contador+=1
    return correctas

def imprimir_ahorcado(equibocado):
       
    if(equibocado == 0):
        print(stages[5])
    elif(equibocado == 1):
        print(stages[4])
    elif(equibocado == 2):
        print(stages[3])
    elif(equibocado == 3):
        print(stages[2])
    elif(equibocado == 4):
        print(stages[1])
    elif(equibocado == 5):
        print(stages[0])

stages = [
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        ''',
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        '''
    ]