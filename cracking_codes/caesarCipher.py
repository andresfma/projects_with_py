'''
What I learned?

the import statement
constans
for loops
if, else, and elif statements
the in and not in operators
the find() string method
'''
import pyperclip

#the message to encrypted/decrypted
message = input('Enter your text: ')

#the encrypted/decrypted key
key = int(input('what\'s your key?: '))

#the program encrypted or decrypted
mode = input('Please choise whether the program Encrypted(e) or decrypted(d): ')

#the possible symbols that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#store the message e/d
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode =='e':
            translatedIndex = symbolIndex + key
        elif mode == 'd':
            translatedIndex = symbolIndex - key
        
        if translatedIndex > len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)   


