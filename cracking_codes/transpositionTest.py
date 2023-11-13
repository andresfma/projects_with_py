'''
what i learned?

random.seet(), random.randint(), random.shuffle() functions and pseudorandom numbers
copy.deepcope para copiar una lista con una nueva referencia
list references

'''

import random, sys, transpositionDecrypt, transpositionEncrypt

def main():
    random.seed(42)

    for i in range(20):

        #generate the random message
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        #convert a list to shuffle it
        message = list(message)

        #shuffle the list
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' %(i + 1, message[:50]))
        
        #check the possible keys
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptedMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            #found a error
            if message != decrypted:
                print('Error in the program, with key: %s and message %s' %(key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
    
    print('Test passed')

#If transpositionTest.py is run...
if __name__ == '__main__':
    main()



