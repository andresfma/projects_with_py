'''
what i learned?

title(), upper(), lower() functions
open(), close(), read(), write()
os module
time module

'''

import time, os, sys, transpositionDecrypt, transpositionEncrypt

def main():
    inputFilename = 'frankenstein.encrypted.txt'
    outputFilename = 'frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'decrypt' #decrypt or encrypt

    #if not exist the input file
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting' %(inputFilename))
        sys.exit()

    #if the output file already exist
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    #read the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' %(myMode.title()))

    #measure how long the e/d takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptedMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round((time.time()-startTime), 2)
    print('%sion time: %s seconds' %(myMode, totalTime))

    #write the translated message in the out file
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters)' %(myMode, inputFilename, len(content)))
    print('%sed file is %s' %(myMode, outputFilename))

#if this file run 
if __name__ == '__main__':
    main()


