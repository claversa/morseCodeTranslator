#Caroline LaVersa
#Morse Code Translator
#12/30/2021

morseAlpha = {
    'a': '.-', 'b':'-...', 'c':'-.-.', 'd': '-..', 'e':'.', 'f':'..-.', 'g':'--.',\
    'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',\
    'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-',\
    'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', ' ': '/'}


def toMorse(sentence):
    '''sentence is a string the user inputs in english. returns a string of
    the morse code version of input sentence.'''
    sentence = sentence.lower()
    morse = ''
    for letter in sentence:
        morse = morse + morseAlpha[letter] + ' '
    return morse


def toEnglish(sentence):
    '''sentence is a string the user inputs in morse code. returns a string 
    of the english version of input sentence.'''
    english = ''
    letters = sentence.split()
    engLet = ''
    for letter in letters:
        for key, value in morseAlpha.items():
            if value == letter:
                engLet = key
        english = english + engLet
    return english
    
