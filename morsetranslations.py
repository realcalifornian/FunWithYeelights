import yeelight
from yeelight import Bulb
import time
myIP = "192.168.0.8" #sets my IP variable, IP will differ based on user's bulb
bulb = Bulb(myIP) #uses the Bulb functionality and ingrains it in the bulb variable

bulb.turn_on(effect="smooth") #turns on our lightbulb

bulb.set_brightness(75) #sets our bulb brightness to a solid 75 off rip

#Imports our dictionary of morse code for specific bulb uses
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(myinput): #defines our encryption function
    cipher = '' #sets up our variable used to implement encrypted code
    for letter in myinput:
        if letter != ' ': #adds our direct translation if there is a letter and adds an extra space to prevent general mesage awkwardness
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: #adds two spaces to show a lack of lettering and change of word, preventing the code from looking confusing
            cipher += ' '
 
    return cipher

def main(): #Defines our main function using our encryption function
    message = input("What's your message?: ")
    result = encrypt(message.upper())
    print(result)

    for i in range(len(result)): #keeps our loop running until our morse code is over
        if result[i] == ".": #sets our bulb color to red when the morse letter is a period
            bulb.set_rgb(255,0,0)
            time.sleep(1)
        elif result[i] == "-": #sets our bulb color to green when the morse letter is a dash
            bulb.set_rgb(0,255,0)
            time.sleep(1)
        else: #sets our bulb color to white when the morse letter is a space, 2 seconds for new letter and 4 for new word
            bulb.set_rgb(1,1,1)
            time.sleep(2)

        i = i + 1 #moves to our next character at the end of the loop
 
# Executes the main function, allowing our word to encrpyt and our light to flicker
if __name__ == '__main__':
    main()
