'''
what i learned?

math.ceil
math.floor
math.round
the true table
boolean operator concatenation
'''
import pyperclip, math

def main():
    myMessage = input('Insert the text to decrypt: ')
    myKey = float(input('Insert the Key: '))

    plaintText = decryptMessage(myKey, myMessage)

    print(plaintText + '|')
    
    pyperclip.copy(plaintText)

def decryptMessage(key, message):
    #calculate the new numbers of rows and columns

    #colums
    numbersColumns = math.ceil(len(message) / key)

    #rows
    numbersRows = int(key)

    #shaded boxes
    numbersShadedBoxes = (numbersRows * numbersColumns) - len(message)

    #generate matrix
    plainText = [''] * numbersColumns

    row = 0
    column = 0
    #the main loop
    for symbol in message:
        plainText[column] += symbol
        column += 1

        #check the numbers of columns available
        if (column == numbersColumns) or ((column == numbersColumns - 1) and (row >= numbersRows - numbersShadedBoxes)):
            row += 1
            column = 0
    
    return ''.join(plainText)

if __name__ == '__main__':
    main()

        
