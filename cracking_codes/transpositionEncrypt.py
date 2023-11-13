'''
what i learned?

main() functions
join() methods
The __name__ variable

'''

import pyperclip

def main():
    myMessage = input('Insert the message to encrypt: ')
    myKey = int(input('Please, insert the key: '))

    cipherText = encryptedMessage(myKey, myMessage)

    print(cipherText + '|')

    pyperclip.copy(cipherText)

def encryptedMessage(key, message):
    cipherText = [''] * key

    #loop llenando la matrix definida por la key y obteniendo el texto cifrado
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]

            currentIndex += key
    
    return ''.join(cipherText)

if __name__ == '__main__':
    main()