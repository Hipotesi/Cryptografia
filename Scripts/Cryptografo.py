#-*- coding: utf-8 -*-
# v =  3.9

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'V',
    '6': 'T',
    '7': 'V',
    '8': 'Y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B'
}

def cypher(message):
    words = message.split(' ') # dividir el message por espacios si hay dos palabras
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)
    
    return ' '.join(cypher_message)

def decipher(message):
    words = message.split(' ') # dividir el message por espacios si hay dos palabras
    decipher_message = [] # en la lista guardamos las palabras que vamos descifrando, la cual reconstruimos al final

    for word in words: 
        decipher_word = ''

        for letter in word: # cada palabra la dividimos en letras por cada iteracion

            for key, value in KEYS.items(): # con items obtenemos la clave y el valor 
                if value == letter: # miramos si cada letra se encuentra en el diccionario
                    decipher_word += key # la llave la metemos dentro de la palabra descifrada (decipher_word) la vamos reconstruyendo
        
        decipher_message.append(decipher_word) # cuando terminamos de reconstruir la palabra la metemos en la lista de palabras

        return ' '.join(decipher_message) # por ultimo las unimos con un espacio y regresamos el mensaje

def run():

    while True:

        command = str(input('''--- * --- * --- * --- * ---

            Bienvenido a criptofrafía. que deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe ty mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)

        elif command == 's':
            print('salir')
        else:
            print('Comando no encontrado!!!')



if __name__ == "__main__":
    print('M E N S A J E S  C I F R A D O S')
    run()